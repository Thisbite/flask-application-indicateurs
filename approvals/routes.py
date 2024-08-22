from flask import Blueprint, render_template, redirect, url_for

approvals = Blueprint('approvals', __name__)

@approvals.route('/<int:id>/approve', methods=['POST'])
def approve_questionnaire(id):
    # Logic to approve the questionnaire
    pass

@approvals.route('/<int:id>/reject', methods=['POST'])
def reject_questionnaire(id):
    # Logic to reject the questionnaire with comments
    pass
