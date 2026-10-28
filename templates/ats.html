{% extends 'base.html' %}
{% block content %}
<div class="row g-4">
    <div class="col-md-4">
        <div class="card">
            <div class="card-body">
                <h4>Jobs</h4>
                <ul class="list-group list-group-flush">
                    {% for item in jobs %}
                    <li class="list-group-item"><a href="{{ url_for('ats.analyze_job', job_id=item.id) }}">{{ item.title }} @ {{ item.company }}</a></li>
                    {% endfor %}
                </ul>
            </div>
        </div>
    </div>
    <div class="col-md-8">
        {% if job %}
        <div class="card mb-4">
            <div class="card-body">
                <h3>{{ job.title }}</h3>
                <p>{{ job.company }} - {{ job.source }}</p>
                <p>{{ job.description[:500] }}</p>
                {% if analysis %}
                <div class="alert alert-info">ATS Match Score: {{ analysis.match_score }}%</div>
                {% endif %}
            </div>
        </div>
        {% endif %}

        {% if resume %}
        <div class="card">
            <div class="card-body">
                <h4>ATS Resume Preview</h4>
                <h5>{{ resume.title }}</h5>
                <p><strong>Summary:</strong> {{ resume.summary }}</p>
                <p><strong>Skills:</strong> {{ resume.technical_skills | join(', ') }}</p>
                <p><strong>Keywords:</strong> {{ resume.keywords | join(', ') }}</p>
                <p><strong>Work Experience:</strong> {{ resume.work_experience }}</p>
                {% if resume.resume_text_preview %}
                <p><strong>Resume content preview:</strong> {{ resume.resume_text_preview[:300] }}</p>
                {% endif %}
            </div>
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}
