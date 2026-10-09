# Division D website — three-contest layout

Install: `python -m pip install -r requirements.txt`
Run: `python -m streamlit run app.py`

Edit CONTESTS in app.py to replace each contest title, date, venue, registration URL and details URL. Put the next upcoming contest first and mark spotlight=True. Empty links appear disabled until configured.

The first tab shows three cards across on desktop, stacking vertically on mobile. The second tab previews Your One-Page Toastmasters Journey and Find a Club. No chatbot is implemented yet.

Keep assets alongside app.py. Each contest currently uses the same included AI-generated photo; change its image field to use another local photo or flyer. Images resolve relative to app.py, regardless of the working directory.

The design_mockup.png file illustrates the three-card arrangement; its example photos differ from the reused packaged photo.
