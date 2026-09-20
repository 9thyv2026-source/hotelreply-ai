import streamlit as st
from google import genai

# 1. Page Configuration
st.set_page_config(page_title="HotelReply AI", page_icon="ðŸ¨", layout="centered")

st.title("ðŸ¨ HotelReply AI Pro")
st.subheader("Generate instant, professional Google Review replies for your hotel!")
st.write("Boost your Google ranking by replying to customers in seconds.")

# 2. User Input Text Areas
review_text = st.text_area("ðŸ“‹ Paste the Customer's Google Review here:")
reply_tone = st.selectbox("ðŸŽ­ Reply Vibe:", ["Professional & Polite", "Warm & Friendly", "Apologetic (For Bad Reviews)"])

# 3. Action Button Trigger
if st.button("âœ¨ Generate Reply"):
    if not review_text:
        st.warning("Please paste a review first!")
    else:
        with st.spinner("AI is writing a professional response..."):
            try:
                # 4. Clean Connected Client Setup
                client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])
                
                # Formatting instructions for the Gemini engine
                prompt_instruction = (
                    f"You are a professional hospitality and hotel manager.\n"
                    f"Write a response to this customer review: '{review_text}'\n"
                    f"Tone of the response: {reply_tone}\n\n"
                    f"Rules:\n"
                    f"- If the review is positive, thank them warmly and invite them back.\n"
                    f"- If the review is negative, apologize professionally, stay polite, and say the management will fix the issue immediately.\n"
                    f"- Keep it concise and professional."
                )
                
                # Using the updated 2026 Gemini 3.6 Flash model
                response = client.models.generate_content(
                    model='gemini-3.6-flash',
                    contents=prompt_instruction,
                )
                
                # 5. Display the Output Response Window
                st.success("âœ”ï¸ Your professional reply is ready to copy:")
                st.text_area("Copy Reply:", value=response.text, height=200)
                
            except Exception as error:
                st.error(f"Something went wrong with the AI connection: {error}")
