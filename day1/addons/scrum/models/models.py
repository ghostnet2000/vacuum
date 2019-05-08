from odoo import fields, models, _


class Sprint(models.Model):
    """Development iteration period."""

    _name = 'sprint'

    name = fields.Char()
    description = fields.Text()
    end = fields.Date()


class Task(models.Model):
    """Unit of work to be done for the sprint."""

    _name = 'task'

    # n.b indexes are integers not strings
    STATUS_TODO = 1
    STATUS_IN_PROGRESS = 2
    STATUS_TESTING = 3
    STATUS_DONE = 4

    STATUS_CHOICES = [
        (STATUS_TODO, _('Not Started')),
        (STATUS_IN_PROGRESS, _('In Progress')),
        (STATUS_TESTING, _('Testing')),
        (STATUS_DONE, _('Done')),
    ]

    name = fields.Char()
    description = fields.Text()
    sprint = fields.One2many('sprint', delegate=True)
    status = fields.Selection(selection=STATUS_CHOICES)
    order = fields.Integer()
    assigned = fields.Char()
    started = fields.Date()
    due = fields.Date()
    completed = fields.Date()

#Task()
#print(dir(Sprint()))
