# NLP-APP 

Web app which lets you to generate word clouds, text summaries and also to check if two text are similar to each other/

## Word clouds
- Upload file or enter text
- Click button to generate word cloud
- You can download your word cloud image in .jpg format

## Text summaries
- Upload file or enter text
- Click button to generate text summary
- You can download your summary in .txt format1

## Text similarity
- Upload files or enter texts
- Click button to check similarity of two texts

## Project structure
Project contains two directories: 
- directory for backend with django
- directory with angular frontend 

## Frameworks and external libraries
- Django
- nltk
- scikit-learn
- numpy
- pandas
- Angular
- angular-material
- dev-extreme

## Run app locally
Clone into git repository by entering `git clone path-to-repository`
Then checkout to frontend/nlp-app folder and run:
`cd frontend/nlp-app`
`ng serve`
Your app should be running on `localhost:8081`

To run Django checkout to backend/mysite and run:
`cd backend/mysite`
`python manage.py runserver`

## Swagger docs
If you run your app locally, to view swagger documentation go to `http://127.0.0.1:8000/docs/`
