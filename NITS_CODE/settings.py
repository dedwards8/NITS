# Django settings for NITS_CODE project.

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    # ('Your Name', 'your_email@example.com'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'NITS',                      # Or path to database file if using sqlite3.
        'USER': 'root',                      # Not used with sqlite3.
        'PASSWORD': 'pword',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Local time zone for this installation. Choices can be found here:
# http://en.wikipedia.org/wiki/List_of_tz_zones_by_name
# although not all choices may be available on all operating systems.
# In a Windows environment this must be set to your system time zone.
TIME_ZONE = 'America/New_York'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

# If you set this to False, Django will make some optimizations so as not
# to load the internationalization machinery.
USE_I18N = True

# If you set this to False, Django will not format dates, numbers and
# calendars according to the current locale.
USE_L10N = True

# If you set this to False, Django will not use timezone-aware datetimes.
USE_TZ = True

# Absolute filesystem path to the directory that will hold user-uploaded files.
# Example: "/home/media/media.lawrence.com/media/"
MEDIA_ROOT = '/home/derek/Code/'

# URL that handles the media served from MEDIA_ROOT. Make sure to use a
# trailing slash.
# Examples: "http://media.lawrence.com/media/", "http://example.com/media/"
MEDIA_URL = 'site_media/'

# Absolute path to the directory static files should be collected to.
# Don't put anything in this directory yourself; store your static files
# in apps' "static/" subdirectories and in STATICFILES_DIRS.
# Example: "/home/media/media.lawrence.com/static/"
STATIC_ROOT = '/home/derek/Code/NITS_CODE/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/NITS_CODE/'

# Additional locations of static files
STATICFILES_DIRS = (
    # Put strings here, like "/home/html/static" or "C:/www/django/static".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/home/derek/Code/NITS_CODE/site_media"
)


# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'i=gffebr=iq+v)ne$lh0e#_-$r(p=t43@fd78=inn$o8(6$rv^'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    # Uncomment the next line for simple clickjacking protection:
    # 'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'NITS_CODE.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'NITS_CODE.wsgi.application'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    "/home/derek/Code/NITS_CODE/templates"
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'hermes',
    # Uncomment the next line to enable the admin:
    # 'django.contrib.admin',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)

# A sample logging configuration. The only tangible logging
# performed by this configuration is to send an email to
# the site admins on every HTTP 500 error when DEBUG=False.
# See http://docs.djangoproject.com/en/dev/topics/logging for
# more details on how to customize your logging configuration.
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
###
#Below is a list of configurables for the project
###Todo: Move these to a separate configurations file
ALPHA = 4.4/1609.34 #Weight associated with VMT in cost function
BETA = 11.4/3600 #Weight associated with Passenger costs in cost function

#Fitness Values
PASSENGER_VOT = 11.4/3600 #Passenger Value of Time $perhour/seconds in hour
FRT_CPM = 9.6/1609.34 #FRT Cost Per Mile $ divided by meters in a mile
DRT_CPM = 4.4/1609.34 #DRT Cost Per Miles $ divided by meters in a mile

#Passenger settings
USE_SURVEY_PASSENGERS = True
SURVEY_PASSENGER_FILE = "hermes/bin/11thru2REAL.csv"
DELETE_SURVEY_PASSENGERS = False #We delete and reload the survey passengers each time
PRESCREEN_PASSENGERS = False #We reconcile passengers that are outside the transit footprint

CREATE_STATIC_TRIPS = False #used in views.py.  If we are debugging and don't to spend a lot of computation time creating static trips, set this to false

#These four variables are used in views.within_coverage_areas
CHECK_GEOFENCING = True #We look at the fenceposts for the subnet

#Isochrones
CHECK_DRIVING_TIME = True #We look at the max driving time for the subnet
CHECK_WALKING_TIME = True #We look at the max walking time for the subnet

#Used for isochrones
CHECK_OTHER_SUBNETS = True # We look to see if other subnets are closer with respect to driving time

#Radius Based
CHECK_RADIUS = False
CHECK_OTHER_SUBNETS_RADIUS = False



DEFAULT_MAX_DRIVING_TIME = 400 #seconds
DEFAULT_MAX_WALKING_TIME = 1000 #seconds

OTP_SERVER_URL = 'http://localhost:8080/'
OSRM_SERVER_URL = 'http://localhost:8001/'
SIMULATION_START_TIME = 11*3600 #seconds into the day
SIMULATION_START_DAY = 17
SIMULATION_START_MONTH = 3
SIMULATION_START_YEAR = 2013
USE_ISOCHRONE_SUBNET = True
USE_CIRCULAR_SUBNET = False

CIRCULAR_SUBNET_RADIUS = 1000 #meters

SIMULATION_LENGTH = 3600*3 #seconds

MANUAL_PSO_INITIALIZATION = False
USE_PSO = True
