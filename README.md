# alyousuf

A Django Project which lists the available jobs that are listed by the users

Setup:
create a virtualenv using virtualenv -p python3 envname<br>
activate virtual environment<br>
**Install Requirements.<br>**
pip install -r requirements.txt<br>

**Run Migrations**<br>
python manage.py migrate.

**Run Server**<br>
python manage.py runserver

**Features**<br>
<li>Landing page with all the jobs listed</li>
<li>We have both list View and Grid View</li>
<li>Logged in User can add job postings in the list view page and also there is an import page where user can copy/paste the data like excel and also can upload the csv file</li>
<li>When copy pasting system excepts coloumns to be identical to model fields, but can be in any order[title,job_description,location,company_name ,phone_number]</li>
<li>A table will be generated as a preview in UI when user copy paste</li>
<li>User can upload csv file.Once uploaded a preview will be shown in the UI and they can confirm</li>
<li>Pagination added for both list view and Grid View</li>
<li>Added import in admin side as well so that admin can add data's in bulk</li>
<li>A form is available in the list page to add job posting</li>

**Scope for Improvement**
<li>we can add more fields like posted-date, posted-by etc.</li>
<li>we can add apply now feature to the application so that we can show the user the option to apply in both list and grid view</li>
<li>can have a menu my job listings so that user can see all the jobs he listed</li>
<li>can have menu applied jobs so that user can see all the jobs he applied</li>
<li>Edit/Delete job postings which is posted by the user</li>
<li>Job description need to be truncated if it has more charecters and can add a detail page</li>
