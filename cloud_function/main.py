from RestrictedPython import compile_restricted
from RestrictedPython.Guards import safe_builtins, safer_getattr, full_write_guard
from RestrictedPython.Eval import default_guarded_getiter
from RestrictedPython.PrintCollector import PrintCollector
from flask import jsonify
import functions_framework

@functions_framework.http
def run_student_code(request):

    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'POST, OPTIONS',
            'Access-Control-Allow-Headers': 'Content-Type',
        }
        return '', 204, headers

    data = request.get_json(silent=True)
    if not data:
        return jsonify({"output": "No JSON payload received"}), 400, {'Access-Control-Allow-Origin': '*'}

    student_code = data.get("student_code", "")
    test_code = data.get("test_code", "")
    full_code = f"{student_code}\n{test_code}"

    sandbox_globals = {
        "__builtins__": safe_builtins,
        "_print_": PrintCollector,
        "_getiter_": default_guarded_getiter,
        "_getattr_": safer_getattr,
        "_write_": full_write_guard,
    }

    try:
        byte_code = compile_restricted(full_code, "<string>", "exec")
        exec(byte_code, sandbox_globals)

        output = sandbox_globals["_print"]()

        return jsonify({"output": output}), 200, {'Access-Control-Allow-Origin': '*'}
    except AssertionError as ae:
        return jsonify({"output": f"❌ Assertion failed: {ae}"}), 200, {'Access-Control-Allow-Origin': '*'}
    except Exception as e:
        return jsonify({"output": f"⚠ Error: {type(e).__name__}: {e}"}), 200, {'Access-Control-Allow-Origin': '*'}
