import streamlit as st
import pandas as pd
import joblib, os

#news_vectorizer = open('models/final_news_cv_vectorizer.pkl', 'rb')
#news_cv = joblib.load()


#load model

nb_model = joblib.load('pipe_temp')
	


def main():
	#st.title("Review Classification")

	st.markdown("<h1 style='text-align: center; color: white;'>Yelp Review Classification</h1>", unsafe_allow_html=True)


	col1, col2, col3 = st.columns([10,20,1])

	with col1:
		st.write("")

	with col2:
		st.image("https://logodix.com/logo/51532.png")

	with col3:
		st.write("")
	#st.markdown("![Alt Text](https://logodix.com/logo/51532.png)")
	st.subheader('Predicting reviews based on NLP')

	activities = ['Prediction', 'NLP']
	choice = st.sidebar.selectbox("Choose Activity",activities)

	if choice == 'predition':
		st.info("predition with ML")

	rev = st.text_area("Enter Review")
	all_ml_model = ['NB', 'NN']
	model_choice = st.selectbox('Choose Model',all_ml_model)
	predction_labels = {'false':0,'true':1}
	if st.button("Classify"):
		test_df =pd.DataFrame([rev],columns =['review'])
		st.text('Original test ::\n{}'.format(rev))
		
		#vect_text = news_cv.transform([rev]).toarray()
		if model_choice == 'NB':
			predictor = nb_model
			pred = predictor.predict(test_df['review'])
			pred_num = pred[0]
			if pred == 1:
				truth = 'True'
			elif pred ==0:
				truth = "False"
			st.write('-------------------')
			st.write(f'This review is most likely {truth}')
			proba = predictor.predict_proba(test_df['review'])
		
			st.write('Probability this review is not Truthful:')
			st.write(((proba[0][1])*100).round(2),'%')
		if model_choice == 'NN':
			pass
	if choice == 'nlp':
		st.info("NLP")

	


if __name__ == '__main__':
	main()