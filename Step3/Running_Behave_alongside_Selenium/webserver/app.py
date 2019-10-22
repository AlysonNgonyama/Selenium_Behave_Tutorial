


from flask import Flask, render_template, url_for, request, redirect
from flask_wtf import Form
from wtforms import TextField, SubmitField, SelectField, validators, PasswordField

class ConfirmForm(Form):
	first_field = TextField('First Name')
	second_field = TextField('Second Name')
	submit = SubmitField('Submit')



app = Flask(__name__)

app.config['SECRET_KEY'] = 'ASODIHG'

@app.route('/success')
def success():
	return render_template('success.html')


@app.route('/', methods=['GET', 'POST'])
def home():
	a_form = ConfirmForm()

	status = False
	if request.method == 'POST':
		print('SO FAR ')
		if a_form.first_field.data == 'First' and a_form.second_field.data == 'Second':
			print("SAODHFOAHSDGOHASOD[GJ[AOPSDJGASJ[DOGJAOSDJ")
			return redirect(url_for('success'))
		else:
			status = True
	return render_template('home.html', a_form=a_form, status=status)



if __name__ == '__main__':
	app.run()
