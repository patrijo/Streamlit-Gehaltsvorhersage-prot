
import joblib
import numpy as np
import streamlit as st

# Modell laden
model_filename = 'linear_regression_model.pkl'  # Lokaler Pfad zur gespeicherten Modell-Datei
model = joblib.load(model_filename)

# Vorhersage für 20 Dienstjahre
jahre_20 = np.array([[20]])
gehalt_20 = model.predict(jahre_20)
print(f"Das vorhergesagte Gehalt für 20 Dienstjahre beträgt: {gehalt_20[0]:.2f} Euro")

# Titel der App
st.title("Gehaltsvorhersage basierend auf Dienstjahren")

# Slider zur Auswahl der Dienstjahre
jahre = st.slider("Wähle die Anzahl der Dienstjahre", 0, 40, 5)

# Vorhersage
jahre_input = np.array([[jahre]])
gehalt = model.predict(jahre_input)

# Ausgabe des Ergebnisses
st.write(f"Das vorhergesagte Gehalt für {jahre} Dienstjahre beträgt: {gehalt[0]:.2f} Euro")

