from flask import Flask, request, abort, jsonify
import os
import sys
import traceback


app = Flask(__name__)


@app.route("/status")
def status():
    return("The Curation Test Plugin Flask Server is up and running")


@app.route("/evaluate", methods=["POST"])
def evaluate():
    data = request.get_json(force=True)
    submit_link = data['submit_link']
    rdf_type = data['type']
    top_level_url = data['top_level']
    complete_sbol = data['complete_sbol']
    instance_url = data['instanceUrl']
    genbank_url = data['genbank']
    size = data['size']
    shallow_sbol = data['shallow_sbol']

    # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~~~~
    # uses rdf types
    accepted_types = {'Activity', 'Agent', 'Association', 'Attachment',
                      'Collection', 'CombinatorialDerivation', 'Component',
                      'ComponentDefinition', 'Cut', 'Experiment',
                      'ExperimentalData', 'FunctionalComponent',
                      'GenericLocation', 'Implementation', 'Interaction',
                      'Location', 'MapsTo', 'Measure', 'Model', 'Module',
                      'ModuleDefinition', 'Participation', 'Plan', 'Range',
                      'Sequence', 'SequenceAnnotation', 'SequenceConstraint',
                      'Usage', 'VariableComponent'}

    acceptable = rdf_type in accepted_types

    # # to ensure it shows up on all pages
    # acceptable = True

    # ------------------------ INTERFACE CREATION ------------------------
    # indicates the format of the interface in the response
    needs_interface = True
    own_interface = False

    # ------------------------ NO INTERFACE ------------------------
    if not needs_interface:
        param_intfc = []
    # -------------------- OWN INTERFACE CREATION ------------------------
    # example of interface creation
    if own_interface and needs_interface:
        cwd = os.getcwd()
        filename = os.path.join(cwd, "Test_Eval.html")

        with open(filename, 'r') as htmlfile:
            param_intfc = htmlfile.read()

            # put in the url, uri, and instance given by synbiohub
            param_intfc = param_intfc.replace("INSTANCE_REPLACE", instance_url)
            param_intfc = param_intfc.replace("SIZE_REPLACE", str(size))
            param_intfc = param_intfc.replace("URI_REPLACE", top_level_url)
            param_intfc = param_intfc.replace("RDFTYPE_REPLACE", rdf_type)
            param_intfc = param_intfc.replace("SHALLOWSBOL_REPLACE", shallow_sbol)
            param_intfc = param_intfc.replace("COMPLETESBOL_REPLACE", complete_sbol)
            param_intfc = param_intfc.replace("GENBANK_REPLACE", genbank_url)
            param_intfc = param_intfc.replace("REQUEST_REPLACE", str(data))
    # ------------------- STANDARD INTERFACE CREATION ------------------------
    # relies on standard converter which uses types based on html form types. Label is the header, description ishelp text, options are possible choices, defaults are what it starts off as, and restrictiosn are any further parameters to add (again based on html form type parameters)
    if not own_interface and needs_interface:
        param_intfc = []
        param_intfc.append({'type': 'text', 'label': 'variable 1', 'description': 'This is variable 1 a text input', 'options': [], 'default': ['default text'], 'restrictions': {}})
        param_intfc.append({'type': 'radio', 'label': 'variable 2', 'description': 'This is variable 2 a radio input', 'options': ['option 1', 'option 2', 'option 3'], 'default': ['option 1'], 'restrictions': {}})
        param_intfc.append({'type': 'checkbox', 'label': 'variable 3', 'description': 'This is variable 3 a checkbox input', 'options': ['option 1', 'option 2', 'option 3'], 'default': ['option 1', 'option 2'], 'restrictions': {}})
        param_intfc.append({'type': 'password', 'label': 'variable 4', 'description': 'This is variable 4 a password input', 'options': [], 'default': [], 'restrictions': {}})
        param_intfc.append({'type': 'reset', 'label': 'variable 5', 'description': 'This is variable 5 a reset button so all values return to default', 'options': [], 'default': [], 'restrictions': {}})
        param_intfc.append({'type': 'color', 'label': 'variable 6', 'description': 'This is variable 6 a colour input', 'options': [], 'default': ['#ffffff'], 'restrictions': {}})
        param_intfc.append({'type': 'date', 'label': 'variable 7', 'description': 'This is variable 7 a date input', 'options': [], 'default': ['2001-11-11'], 'restrictions': {'min': '2000-01-01', 'max': '2020-01-01'}})
        param_intfc.append({'type': 'date', 'label': 'variable 8', 'description': 'This is variable 8 a date-time-local input', 'options': [], 'default': ['2001-11-11'], 'restrictions': {}})
        param_intfc.append({'type': 'email', 'label': 'variable 9', 'description': 'This is variable 9 an email input', 'options': [], 'default': ['test@gmail.com'], 'restrictions': {}})
        param_intfc.append({'type': 'file', 'label': 'variable 10', 'description': 'This is variable 10 a file input', 'options': [], 'default': [], 'restrictions': {}})
        param_intfc.append({'type': 'month', 'label': 'variable 11', 'description': 'This is variable 11 a month input', 'options': [], 'default': ['2020-07'], 'restrictions': {}})
        param_intfc.append({'type': 'number', 'label': 'variable 12', 'description': 'This is variable 12 a number input', 'options': [], 'default': [7.89], 'restrictions': {}})
        param_intfc.append({'type': 'range', 'label': 'variable 13', 'description': 'This is variable 13 a range input', 'options': [], 'default': [], 'restrictions': {}})
        param_intfc.append({'type': 'tel', 'label': 'variable 14', 'description': 'This is variable 14 a tel input', 'options': [], 'default': ['888-88-888'], 'restrictions': {'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{3}'}})
        param_intfc.append({'type': 'time', 'label': 'variable 15', 'description': 'This is variable 15 a time input', 'options': [], 'default': ['16:30'], 'restrictions': {}})
        param_intfc.append({'type': 'url', 'label': 'variable 16', 'description': 'This is variable 16 a url input', 'options': [], 'default': ['http://www.awesome.com'], 'restrictions': {}})
        param_intfc.append({'type': 'week', 'label': 'variable 17', 'description': 'This is variable 17 a week input', 'options': [], 'default': ['2011-W20'], 'restrictions': {}})
    # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

    if acceptable:
        response = {'needs_interface': needs_interface, 'own_interface': own_interface, 'submit_link': submit_link, 'interface': param_intfc}
        # return f'The type sent ({rdf_type}) is an accepted type', 200
        return jsonify(response)

    else:
        return f'The type sent ({rdf_type}) is NOT an accepted type', 415


@app.route("/run", methods=["POST"])
def run():
    data = request.get_json(force=True)

    submit_link = data['submit_link']
    eval_params = data['eval_parameters']
    top_level_url = data['top_level']
    complete_sbol = data['complete_sbol']
    genbank_url = data['genbank']
    instance_url = data['instanceUrl']
    size = data['size']
    rdf_type = data['type']
    shallow_sbol = data['shallow_sbol']

    try:
        # ~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~~~~~
        # ------------------------ INTERFACE CREATION ------------------------
        # indicates the format of the interface in the response
        needs_interface = True
        own_interface = True

        # ------------------------ NO INTERFACE ------------------------
        if not needs_interface:
            run_intfc = []

        # -------------------- OWN INTERFACE CREATION ------------------------
        # example of interface creation
        if own_interface and needs_interface:
            cwd = os.getcwd()
            filename = os.path.join(cwd, "Test_Run.html")

            with open(filename, 'r') as htmlfile:
                run_intfc = htmlfile.read()

                # put in the url, uri, and instance given by synbiohub
                run_intfc = run_intfc.replace("SIZE_REPLACE", str(size))
                run_intfc = run_intfc.replace("URI_REPLACE", top_level_url)
                run_intfc = run_intfc.replace("RDFTYPE_REPLACE", rdf_type)
                run_intfc = run_intfc.replace("SHALLOWSBOL_REPLACE", shallow_sbol)
                run_intfc = run_intfc.replace("COMPLETESBOL_REPLACE", complete_sbol)
                run_intfc = run_intfc.replace("INSTANCE_REPLACE", instance_url)
                run_intfc = run_intfc.replace("REQUEST_REPLACE", str(data))
                run_intfc = run_intfc.replace("GENBANK_REPLACE", genbank_url)
                run_intfc = run_intfc.replace("PARAMETERS_REPLACE", str(eval_params))

        # ------------------- STANDARD INTERFACE CREATION ---------------------
        # relies on standard converter which uses types based on html form
        # types. Label is the header, description ishelp text, options are
        # possible choices, defaults are what it starts off as, and
        # restrictiosn are any further parameters to add (again based on
        # html form type parameters)
        if not own_interface and needs_interface:
            run_intfc = []
            run_intfc.append({'type': 'text', 'label': 'variable 1', 'description': 'This is variable 1 a text input', 'options': [], 'default': ['default text'], 'restrictions': {}})
            run_intfc.append({'type': 'radio', 'label': 'variable 2', 'description': 'This is variable 2 a radio input', 'options': ['option 1', 'option 2', 'option 3'], 'default': ['option 1'], 'restrictions': {}})
            run_intfc.append({'type': 'checkbox', 'label': 'variable 3', 'description': 'This is variable 3 a checkbox input', 'options': ['option 1', 'option 2', 'option 3'], 'default': ['option 1', 'option 2'], 'restrictions': {}})
            run_intfc.append({'type': 'password', 'label': 'variable 4', 'description': 'This is variable 4 a password input', 'options': [], 'default': [], 'restrictions': {}})
            run_intfc.append({'type': 'reset', 'label': 'variable 5', 'description': 'This is variable 5 a reset button so all values return to default', 'options': [], 'default': [], 'restrictions': {}})
            run_intfc.append({'type': 'color', 'label': 'variable 6', 'description': 'This is variable 6 a colour input', 'options': [], 'default': ['#ffffff'], 'restrictions': {}})
            run_intfc.append({'type': 'date', 'label': 'variable 7', 'description': 'This is variable 7 a date input', 'options': [], 'default': ['2001-11-11'], 'restrictions': {'min': '2000-01-01', 'max': '2020-01-01'}})
            run_intfc.append({'type': 'date', 'label': 'variable 8', 'description': 'This is variable 8 a date-time-local input', 'options': [], 'default': ['2001-11-11'], 'restrictions': {}})
            run_intfc.append({'type': 'email', 'label': 'variable 9', 'description': 'This is variable 9 an email input', 'options': [], 'default': ['test@gmail.com'], 'restrictions': {}})
            run_intfc.append({'type': 'file', 'label': 'variable 10', 'description': 'This is variable 10 a file input', 'options': [], 'default': [], 'restrictions': {}})
            run_intfc.append({'type': 'month', 'label': 'variable 11', 'description': 'This is variable 11 a month input', 'options': [], 'default': ['2020-07'], 'restrictions': {}})
            run_intfc.append({'type': 'number', 'label': 'variable 12', 'description': 'This is variable 12 a number input', 'options': [], 'default': [7.89], 'restrictions': {}})
            run_intfc.append({'type': 'range', 'label': 'variable 13', 'description': 'This is variable 13 a range input', 'options': [], 'default': [], 'restrictions': {}})
            run_intfc.append({'type': 'tel', 'label': 'variable 14', 'description': 'This is variable 14 a tel input', 'options': [], 'default': ['888-88-888'], 'restrictions': {'pattern': '[0-9]{3}-[0-9]{2}-[0-9]{3}'}})
            run_intfc.append({'type': 'time', 'label': 'variable 15', 'description': 'This is variable 15 a time input', 'options': [], 'default': ['16:30'], 'restrictions': {}})
            run_intfc.append({'type': 'url', 'label': 'variable 16', 'description': 'This is variable 16 a url input', 'options': [], 'default': ['http://www.awesome.com'], 'restrictions': {}})
            run_intfc.append({'type': 'week', 'label': 'variable 17', 'description': 'This is variable 17 a week input', 'options': [], 'default': ['2011-W20'], 'restrictions': {}})
        # ~~~~~~~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
        if needs_interface:
            response = {'needs_interface': needs_interface,
                        'own_interface': own_interface,
                        'submit_link': submit_link, 'interface': run_intfc}
            return jsonify(response)
    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        lnum = exc_tb.tb_lineno
        abort(400, f'Exception is: {e}, exc_type: {exc_type}, exc_obj: {exc_obj}, fname: {fname}, line_number: {lnum}, traceback: {traceback.format_exc()}')


@app.route("/save", methods=["POST"])
def save():
    data = request.get_json(force=True)

    eval_params = data['eval_parameters']
    run_params = data['run_parameters']
    top_level_url = data['top_level']
    complete_sbol = data['complete_sbol']
    genbank_url = data['genbank']
    instance_url = data['instanceUrl']
    size = data['size']
    rdf_type = data['type']
    shallow_sbol = data['shallow_sbol']

    try:
        # ~~~~~~~~~~~~~ REPLACE THIS SECTION WITH OWN RUN CODE ~~~~~~~~~~~~
        cwd = os.getcwd()
        file_path = os.path.join(cwd, "Test.xml")

        # read in Test.xml
        with open(file_path, 'r') as xmlfile:
            result = xmlfile.read()

        # put in the url, filename, and instance given by synbiohub
        result = result.replace("SIZE_REPLACE", str(size))
        result = result.replace("URI_REPLACE", top_level_url)
        result = result.replace("RDFTYPE_REPLACE", rdf_type)
        result = result.replace("SHALLOWSBOL_REPLACE", shallow_sbol)
        result = result.replace("COMPLETESBOL_REPLACE", complete_sbol)
        result = result.replace("INSTANCE_REPLACE", instance_url)
        result = result.replace("GENBANK_REPLACE", genbank_url)
        result = result.replace("REQUEST_REPLACE", str(data))
        updated_sbol = result.replace("EVAL_PARAMETERS_REPLACE", str(eval_params))
        updated_sbol = result.replace("RUN_PARAMETERS_REPLACE", str(run_params))
        # ~~~~~~~~~~~~~~~~~~~~ END SECTION ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        return updated_sbol

    except Exception as e:
        exc_type, exc_obj, exc_tb = sys.exc_info()
        fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
        lnum = exc_tb.tb_lineno
        abort(415, f'Exception is: {e}, exc_type: {exc_type}, exc_obj: {exc_obj}, fname: {fname}, line_number: {lnum}, traceback: {traceback.format_exc()}')
