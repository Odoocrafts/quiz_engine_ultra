from odoo import api, fields, models, _


class Quiz(models.Model):
    _name = 'quiz.quiz'
    _description = 'Quiz'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)
    description = fields.Text(string='Description')
    active = fields.Boolean(string='Active', default=True)
    question_ids = fields.One2many('quiz.question', 'quiz_id', string='Questions')
    type = fields.Selection(
        [('practice', 'Practice Quiz'), ('test', 'Assessment Test')],
        string='Type', default='practice', required=True
    )
    attempts_allowed = fields.Integer(
        string='Attempts Allowed', 
        default=0,
        help="Maximum number of attempts allowed. Set to 0 for unlimited attempts."
    )
    
    # Sprint 1: Added instruction screen and timer fields
    instruction_text = fields.Html(
        string='Instructions',
        help="Instructions to show before the quiz begins"
    )
    timer_type = fields.Selection(
        [
            ('none', 'No Time Limit'),
            ('global', 'Global Time Limit'),
            ('per_question', 'Time per Question')
        ],
        string='Timer Type',
        default='none',
        required=True
    )
    global_time_limit = fields.Integer(
        string='Global Time Limit (minutes)',
        default=30,
        help="Total time in minutes for the entire quiz"
    )
    per_question_time = fields.Integer(
        string='Time per Question (seconds)',
        default=60,
        help="Time allowed for each question in seconds"
    )


class QuizQuestion(models.Model):
    _name = 'quiz.question'
    _description = 'Quiz Question'
    _order = 'sequence, id'

    quiz_id = fields.Many2one('quiz.quiz', string='Quiz', required=True, ondelete='cascade')
    name = fields.Char(string='Title', required=True)
    question_text = fields.Html(string='Question Text', sanitize=True)
    question_type = fields.Selection([
        ('mcq', 'Multiple Choice'),
        ('text', 'Text Input'),
        ('fill_blank', 'Fill in the Blanks'),
        ('drag_order', 'Drag and Order')
    ], string='Question Type', default='mcq', required=True)
    answer_ids = fields.One2many('quiz.answer', 'question_id', string='Answers')
    sequence = fields.Integer(string='Sequence', default=10)


class QuizAnswer(models.Model):
    _name = 'quiz.answer'
    _description = 'Quiz Answer'
    _order = 'sequence, id'

    question_id = fields.Many2one('quiz.question', string='Question', required=True, ondelete='cascade')
    answer_text = fields.Text(string='Answer Text', required=True)
    is_correct = fields.Boolean(string='Is Correct')
    score = fields.Float(string='Score', default=1.0)
    sequence = fields.Integer(string='Sequence', default=10)
