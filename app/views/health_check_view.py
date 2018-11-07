from app import application

@application.route('/health_check', methods=['GET'])
def health_check():
    return '', 200, {}