from odoo import models, fields, api
from odoo.exceptions import ValidationError


class TodoList(models.Model):
    _name = 'todo.list'
    _description = 'Todo List'

    name = fields.Char(required=True, string='Title')
    tag_ids = fields.Many2many('todo.tag', string='Tags')
    start_date = fields.Datetime(required=True, string='Start Date & Time')
    end_date = fields.Datetime(required=True, string='End Date & Time')
    status = fields.Selection([
        ('draft', 'Draft'),
        ('in_progress', 'In Progress'),
        ('complete', 'Complete')
    ], default='draft', string='Status')

    item_ids = fields.One2many('todo.item', 'todo_id', string='Items')
    participant_ids = fields.Many2many('res.users', string='Attendees')
    completed = fields.Boolean(string='Completed', default=False)

    show_start_button = fields.Boolean(
        compute='_compute_show_buttons',
        store=False,
        string='Show Start Button'
    )
    show_done_button = fields.Boolean(
        compute='_compute_show_buttons',
        store=False,
        string='Show Done Button'
    )

    @api.depends('status', 'item_ids.completed')
    def _compute_show_buttons(self):
        for rec in self:
            rec.show_start_button = rec.status == 'draft' and not rec.completed
            rec.show_done_button = (
                rec.status == 'in_progress'
                and rec.item_ids
                and all(item.completed for item in rec.item_ids)
            )

    @api.constrains('start_date', 'end_date')
    def _check_dates(self):
        for rec in self:
            if rec.end_date < rec.start_date:
                raise ValidationError('End date must be after start date')

    def action_start_progress(self):
        for rec in self:
            if rec.status == 'draft':
                rec.status = 'in_progress'

    def action_mark_complete(self):
        for rec in self:
            if rec.item_ids and all(item.completed for item in rec.item_ids):
                rec.status = 'complete'
                rec.completed = True


class TodoItem(models.Model):
    _name = 'todo.item'
    _description = 'Todo List Item'

    todo_id = fields.Many2one('todo.list', required=True, ondelete='cascade')
    name = fields.Char(required=True, string='Task')
    description = fields.Text(string='Description')
    completed = fields.Boolean(string='Is Complete', default=False)

    @api.onchange('completed')
    def _onchange_completed(self):
        if self.completed and self.todo_id.status != 'in_progress':
            self.completed = False
            raise ValidationError(
                'Items can only be marked complete in In Progress status.'
            )

    @api.model
    def create(self, vals):
        todo = self.env['todo.list'].browse(vals.get('todo_id'))
        if todo.status == 'complete':
            raise ValidationError('Cannot add items to a completed Todo List.')
        return super(TodoItem, self).create(vals)


class TodoTag(models.Model):
    _name = 'todo.tag'
    _description = 'Tags for Todo'
    _rec_name = 'name'

    name = fields.Char(required=True, string='Tag Name')