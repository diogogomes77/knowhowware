# knowhowware

This platform aims to provide a searchabled database of project participations with details about used technologies and related issues during development.

## Deployment:

It uses Docker and can be started with `docker-compose up`

### To-do list:
- [x] model Project + admin
- [x] model Participant + admin
- [x] model Participation + admin
- [x] model Technology + admin
add to the through model an explanation about how the tech was used in the project
- [x] model Participation + admin
- [x] initial data fixture
- [x] PostgreSQL
- [x] Docker setup
- [ ] Dashboard HTML template
- [ ] Dashboard React template
- [x] PDF report generator from HTML template
- [ ] PDF report with content options
- [x] Tags in projects and technologies (tool, language, framework, etc)
- [ ] Track visitors
- [x] DRF integration with React
- [ ] DRF integration with JWT
- [x] Celery integration (async task)
- [ ] Celery integration (periodic task)
- [ ] Channels integration with template frontend
- [ ] Channels integration with React
- [x] Technology multi parent
- [x] User Participant registration admin form
- [x] REST Swagger
- [ ] STOMP + JWT + Channels
- [ ] Multiple links (using generic many-to-many rels)
- [ ] ElasticSearch
- [ ] Google Cloud