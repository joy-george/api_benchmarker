import connexion, argparse, json, time
from flask import g,jsonify, request

from config import app_config
from swagger_ui_bundle import swagger_ui_3_path

options = {'swagger_path': swagger_ui_3_path}
app = connexion.App(__name__,
                    specification_dir='./',
                    options=options)

# Read the swagger.yml file to configure the endpoints
app.add_api('swagger.yml')

def add_response_time(func):
    def modify_response(response):
        # Can probably set a property in the response object for
        # which the response time needs to be calculated.
        if request.endpoint != "/api.api_timer_get_current_time":
            return response

        modified_response_data = json.loads(response.get_data(as_text=True))
        # x 1000 to convert the output into milliseconds
        modified_response_data["responseTimeMs"] = "{:.4f}".format((time.time() - g.start_time) * 1000)

        return func(jsonify(modified_response_data))

    return modify_response


@app.app.before_request
def set_response_start_time():
    g.start_time = time.time()


@app.app.after_request
@add_response_time
def call_after_request_callbacks(response):
    return response

@app.app.errorhandler(404)
def page_not_found(e):
    return jsonify({"error" : "Not Found"})

def check_valid_env(env):
    try:
        app_config[env]
    except:
        raise argparse.ArgumentTypeError("{environment} is an invalid environment value".
                                         format(environment = env))
    return env

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='To fetch application environment')
    parser.add_argument('--env',
                        dest='env',
                        default='development',
                        type=check_valid_env,
                        help='Environment can either be production or development. Default is development.')

    args = parser.parse_args()
    app_env = args.env
    app.run(host=app_config[app_env].HOST,
            port=app_config[app_env].PORT,
            debug=app_config[app_env].DEBUG)
