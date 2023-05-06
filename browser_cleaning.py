from flask import Flask, render_template, url_for, request, jsonify
import web_Gmail_cleaning_service as clean

app = Flask(__name__, static_url_path='/static')
app.config['DEBUG']=True

@app.route('/', methods=['GET', 'POST'])
def index():
    service = clean.get_service()
    if request.method == 'POST':
        print(request.method)
        # Retrieve form data
        label = request.form['label-dropdown']
        num_emails = int(request.form['number-input'])
        
        # if they ask for more than 500 - which is the list() limit - there should be multiple calls
        while num_emails > 500:
            count = 1
            print(f"Deleting batch number {count}")
            message_ids = clean.get_emails(service, num_emails, label)
            response = clean.delete_emails(service, message_ids)
            if response:  # The response is empty
                print("Messages deleted: SUCCESS")
            num_emails += -500
            count += 1

        # collect emails from the label and number of emails        
        msg_ids = clean.get_emails(service, num_emails, label)

        # Delete command
        response = clean.delete_emails(service, msg_ids)
        return render_template('delete_mails.html', labels_list=label, response=response)

    else:
        # Render the template with the form
        label_list = clean.show_labels(service)

        return render_template('delete_mails.html', label_list=label_list)
@app.route('/get_data')
def get_data():
    service = clean.get_service()
    # Code to generate the data
    labels_list = clean.show_labels(service)
    label_dict = {}
    for label in labels_list:
        label_dict[label] = clean.count_pages(service, label)

    # Return the data in JSON format
    return jsonify(label_dict)

if __name__ == '__main__':
    app.run()
