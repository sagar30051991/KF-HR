# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "kf"
app_title = "kf"
app_publisher = "Indictrans"
app_description = "HR "
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "sagar.s@indictransech.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/kf/css/kf.css"
# app_include_js = "/assets/kf/js/kf.js"

# include js, css files in header of web template
# web_include_css = "/assets/kf/css/kf.css"
# web_include_js = "/assets/kf/js/kf.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "kf.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "kf.install.before_install"
# after_install = "kf.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "kf.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"kf.tasks.all"
# 	],
# 	"daily": [
# 		"kf.tasks.daily"
# 	],
# 	"hourly": [
# 		"kf.tasks.hourly"
# 	],
# 	"weekly": [
# 		"kf.tasks.weekly"
# 	]
# 	"monthly": [
# 		"kf.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "kf.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "kf.event.get_events"
# }

