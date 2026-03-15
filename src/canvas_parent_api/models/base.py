"""Base Model Definition."""
from typing import Optional
from pydantic import BaseModel, Field


class ObserveeResponse(BaseModel):
    """Observee Response Definition."""
    id: int
    name: str
    created_at: str
    sortable_name: str
    short_name: str
    observation_link_root_account: Optional[list[int]] = None


class CourseResponse(BaseModel):
    """Course Response Definition."""
    class Config:
        exclude = ['sis_course_id', 'uuid',
                   'integration_id', 'sis_import_id',
                   'workflow_state', 'account_id',
                   'root_account_id', 'grade_passback_setting',
                   'locale', 'total_students',
                   'default_view', 'needs_grading_count',
                   'apply_assignment_group_weights', 'permissions',
                   'is_public', 'is_public_to_auth_users',
                   'public_syllabus_to_auth', 'storage_quota_mb',
                   'storage_quota_used_mb', 'hide_final_grades',
                   'license', 'allow_student_assignment_edits',
                   'allow_wiki_comments', 'allow_student_forum_attachments',
                   'restrict_enrollments_to_course_dates', 'access_restricted_by_date',
                   'blueprint', 'blueprint_restrictions',
                   'blueprint_restrictions_by_object_type', 'template']
    id: int
    name: Optional[str] = None
    course_code: Optional[str] = None
    original_name: Optional[str] = None
    enrollment_term_id: Optional[int] = None
    grading_periods: Optional[list] = Field([None])
    grading_standard_id: Optional[int] = Field(None)
    created_at: Optional[str] = None
    start_at: Optional[str] = Field(None)
    end_at: Optional[str] = Field(None)
    enrollments: Optional[list] = Field([None])
    calendar: Optional[dict] = None
    syllabus_body: Optional[str] = None
    term: Optional[dict] = None
    course_progress: Optional[int] = None
    public_syllabus: Optional[bool] = None
    public_description: Optional[str] = None
    open_enrollment: Optional[bool] = None
    self_enrollment: Optional[bool] = None
    course_format: Optional[str] = None
    time_zone: Optional[str] = None


class AssignmentResponse(BaseModel):
    """Assignment Response Definition"""
    class Config:
        exclude = ['has_overrides', 'all_dates',
                   'html_url', 'submission_download_url',
                   'assignment_group_id', 'due_date_required',
                   'allowed_extensions', 'max_name_length',
                   'turnitin_enabled', 'vericite_enabled',
                   'turnitin_settings', 'grade_group_students_individually',
                   'external_tool_tag_attributes', 'peer_reviews',
                   'autoamtic_peer_reviews', 'peer_review_count',
                   'peer_reviews_assign_at', 'intra_group_peer_reviews',
                   'group_category_id', 'needs_grading_count',
                   'needs_grading_count_by_section', 'position',
                   'post_to_sis', 'integration_id',
                   'integration_data', 'submission_types',
                   'grading_type', 'grading_standard_id',
                   'published', 'unpublishable',
                   'only_visible_to_overrides', 'locked_for_user',
                   'locked_info', 'lock_explanation',
                   'anonymous_submissions', 'freeze_on_copy',
                   'frozen', 'frozen_attributes',
                   'use_rubric_for_grading', 'rubric_settings',
                   'assignment_visibility', 'overrides',
                   'omit_from_final_grade', 'moderated_grading',
                   'grader_count', 'final_grader_id',
                   'grader_comments_visible_to_graders',
                   'graders_anonymous_to_graders', 'anonymous_grading',
                   'post_manually', 'score_statistics',
                   'annotatable_attachment_id', 'anonymize_students',
                   'require_lockdown_browser', 'muted']
    id: int
    name: Optional[str] = None
    description: Optional[str] = Field(None)
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    due_at: Optional[str] = None
    lock_at: Optional[str] = None
    unlock_at: Optional[str] = None
    course_id: Optional[int] = None
    points_possible: Optional[float] = None
    has_submitted_submissions: Optional[bool] = None
    quiz_id: Optional[int] = None
    discussion_topic: Optional[dict] = None
    submission: Optional[dict] = None
    rubric: Optional[list] = Field([None])
    can_submit: Optional[bool] = None
    important_dates: Optional[bool] = None


class SubmissionResponse(BaseModel):
    """Submission Response Definition"""
    class Config:
        exclude = ['assignment', 'course',
                   'html_url', 'preview_url',
                   'submission_type', 'url',
                   'user_id', 'grader_id',
                   'user', 'assignment_visible',
                   'extra_attempts', 'anonymous_id',
                   'posted_at', 'read_status',
                   'redo_request']
    assignment_id: int
    attempt: Optional[int] = None
    body: Optional[str] = None
    grade: Optional[str] = None
    grade_matches_current_submission: Optional[bool] = None
    score: Optional[float] = None
    submission_comments: Optional[str] = None
    submitted_at: Optional[str] = None
    late: Optional[bool] = None
    excused: Optional[bool] = None
    missing: Optional[bool] = None
    late_policy_status: Optional[str] = None
    points_deducted: Optional[float] = None
    workflow_state: Optional[str] = None
