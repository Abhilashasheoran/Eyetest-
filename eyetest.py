import streamlit as st
from PIL import Image
import random

# ---------------- Page Setup ----------------
st.set_page_config(page_title="👁️ Eye Diagnosis Simulator", layout="centered")
st.title("👁️ AI Eye Check - Demo Simulator")
st.markdown("Upload a picture of each eye to simulate a vision diagnosis and get a mock prescription.")

# ---------------- Image Upload ----------------
left_eye = st.file_uploader("📤 Upload LEFT eye image", type=["jpg", "jpeg", "png"], key="left")
right_eye = st.file_uploader("📤 Upload RIGHT eye image", type=["jpg", "jpeg", "png"], key="right")

# ---------------- Submit Button ----------------
if st.button("🩺 Analyze & Generate Prescription"):
    if not left_eye or not right_eye:
        st.warning("Please upload both eye images to proceed.")
    else:
        st.success("✅ Images received. Simulating diagnosis...")

        # Simulate processing
        st.image(Image.open(left_eye), caption="Left Eye", width=250)
        st.image(Image.open(right_eye), caption="Right Eye", width=250)

        # ---------------- Simulated Results ----------------
        def fake_prescription():
            sphere = round(random.uniform(-4.0, +1.0), 2)
            cylinder = round(random.uniform(-2.0, 0), 2)
            axis = random.randint(0, 180)
            return sphere, cylinder, axis

        l_sphere, l_cylinder, l_axis = fake_prescription()
        r_sphere, r_cylinder, r_axis = fake_prescription()

        st.subheader("👓 Simulated Eye Prescription")
        st.markdown(f"""
        #### 🦶 Left Eye (OS):
        - Sphere: `{l_sphere} D`
        - Cylinder: `{l_cylinder} D`
        - Axis: `{l_axis}°`

        #### ✋ Right Eye (OD):
        - Sphere: `{r_sphere} D`
        - Cylinder: `{r_cylinder} D`
        - Axis: `{r_axis}°`
        """)

        # ---------------- Feedback ----------------
        st.divider()
        st.subheader("📋 Feedback & Recommendation")

        if l_sphere < -2 or r_sphere < -2:
            st.warning("🔎 You may have moderate myopia (nearsightedness). Avoid screen glare and check lighting.")
        elif l_sphere > 0 or r_sphere > 0:
            st.info("🔍 Mild hyperopia (farsightedness) detected. Consider eye strain management.")

        if abs(l_cylinder) > 1 or abs(r_cylinder) > 1:
            st.warning("🌀 Possible signs of astigmatism. You might need toric lenses.")

        st.success("📅 This is a simulated result. For accurate prescriptions, visit a licensed optometrist.")

# ---------------- Footer ----------------
st.markdown("---")
st.caption("⚠️ This is a demo app. I hope it helps you.")