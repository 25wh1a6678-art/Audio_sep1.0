import streamlit as st

st.title("AudioSep — Text-Guided Audio Separation")

uploaded = st.file_uploader("Upload a mixed audio file", type=["wav", "mp3"])
prompt = st.text_input("Describe the sound to extract", placeholder="e.g. human speech")

if st.button("Separate"):
    if not uploaded:
        st.error("Please upload an audio file.")
    elif not prompt.strip():
        st.error("Please enter a prompt.")
    else:
        import tempfile, os
        from inference import separate

        with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as tmp_in:
            tmp_in.write(uploaded.read())
            input_path = tmp_in.name

        output_path = input_path.replace(".wav", "_out.wav")

        try:
            with st.spinner("Separating..."):
                separate(input_path, prompt.strip(), output_path)
            st.session_state["output_path"] = output_path
            st.session_state["input_path"] = input_path
        except Exception as e:
            st.error(f"Inference failed: {e}")
        finally:
            pass  # keep temp files for playback
