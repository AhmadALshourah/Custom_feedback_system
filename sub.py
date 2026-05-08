import pandas as pd

def get_data(s,e):
    data = pd.read_csv("../../Pycharm/PythonProject1/Feedback.csv")
    complaints = data.iloc[s:e]
    return complaints["Complaints"]

def add_data(complaint,category,keywords):
    existing_data = pd.read_csv("../../Pycharm/PythonProject1/results.csv")
    keywords_with_dash = [k.replace(",", "-") for k in keywords]
    new_data = pd.DataFrame({
        "Complaint": complaint,
        "Category": category,
        "Keywords": keywords_with_dash
    })
    combined_data =pd.concat([existing_data,new_data], ignore_index=True)
    combined_data.to_csv("results.csv", index= False)
