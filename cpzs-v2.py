import tkinter as tk
from tkinter import messagebox

# 定义计算函数
def calculate_chlorpromazine_equivalent(drug, dose):
    # 药物信息
    antipsychotics = {
        "acepromazine": {"en": "acepromazine", "zh": "乙酰普罗马嗪", "factor": 3},
        "acetophenazine": {"en": "acetophenazine", "zh": "乙酰苯哌嗪", "factor": 6},
        "amisulpride": {"en": "amisulpride", "zh": "氨磺必利", "factor": 0.75},
        "aripiprazole": {"en": "aripiprazole", "zh": "阿立哌唑", "factor": 20},
        "asenapine": {"en": "asenapine", "zh": "阿塞那平", "factor": 15},
        "benperidol": {"en": "benperidol", "zh": "苯哌利多", "factor": 200},
        "bromperidol": {"en": "bromperidol", "zh": "溴哌利多", "factor": 30},
        "cariprazine": {"en": "cariprazine", "zh": "卡立普嗪", "factor": 30},
        "chlorpromazine": {"en": "chlorpromazine", "zh": "氯丙嗪", "factor": 1},
        "chlorprothixene": {"en": "chlorprothixene", "zh": "氯丙噻吨", "factor": 1},
        "clopenthixol": {"en": "clopenthixol", "zh": "氯喷噻吨", "factor": 3},
        "clotiapine": {"en": "clotiapine", "zh": "氯噻平", "factor": 3.75},
        "clozapine": {"en": "clozapine", "zh": "氯氮平", "factor": 1},
        "flupentixol": {"en": "flupentixol", "zh": "氟哌噻吨", "factor": 50},
        "fluphenazine": {"en": "fluphenazine", "zh": "氟奋乃静", "factor": 30},
        "fluspirilen": {"en": "fluspirilen", "zh": "氟司必林", "factor": 1},  # Factor not provided in the image, default to 1
        "haloperidol": {"en": "haloperidol", "zh": "氟哌啶醇", "factor": 37.5},
        "levomepromazine": {"en": "levomepromazine", "zh": "左美普嗪", "factor": 1},
        "loxapine": {"en": "loxapine", "zh": "洛沙平", "factor": 3},
        "lurasidone": {"en": "lurasidone", "zh": "鲁拉西酮", "factor": 5},
        "melperone": {"en": "melperone", "zh": "美普仑", "factor": 1},
        "mesoridazine": {"en": "mesoridazine", "zh": "美索达嗪", "factor": 1.5},
        "molindone": {"en": "molindone", "zh": "莫林酮", "factor": 6},
        "moperone": {"en": "moperone", "zh": "吗哌隆", "factor": 15},
        "olanzapine": {"en": "olanzapine", "zh": "奥氮平", "factor": 30},
        "oxypertine": {"en": "oxypertine", "zh": "奥克舍平", "factor": 2.5},
        "paliperidone": {"en": "paliperidone", "zh": "帕利哌酮", "factor": 50},
        "penfluridol": {"en": "penfluridol", "zh": "喷氟利多", "factor": 50},
        "perazine": {"en": "perazine", "zh": "哌拉嗪", "factor": 3},
        "periciazine": {"en": "periciazine", "zh": "哌氯嗪", "factor": 6},
        "perphenazine": {"en": "perphenazine", "zh": "奋乃静", "factor": 10},
        "pimozide": {"en": "pimozide", "zh": "匹莫齐特", "factor": 75},
        "pipamperone": {"en": "pipamperone", "zh": "匹帕佩隆", "factor": 1.5},
        "pipotiazine": {"en": "pipotiazine", "zh": "匹泊噻嗪", "factor": 30},
        "prochlorperazine": {"en": "prochlorperazine", "zh": "普鲁氯嗪", "factor": 3},
        "promazine": {"en": "promazine", "zh": "异丙嗪", "factor": 1},
        "prothipendyl": {"en": "prothipendyl", "zh": "普罗噻吡", "factor": 1.25},
        "quetiapine": {"en": "quetiapine", "zh": "喹硫平", "factor": 0.75},
        "remoxipride": {"en": "remoxipride", "zh": "瑞莫西利", "factor": 1},
        "risperidone": {"en": "risperidone", "zh": "利培酮", "factor": 60},
        "sertindole": {"en": "sertindole", "zh": "舍萘酮", "factor": 18.75},
        "sulpiride": {"en": "sulpiride", "zh": "舒必利", "factor": 0.375},
        "sultopiride": {"en": "sultopiride", "zh": "舒托必利", "factor": 0.25},
        "thiopropazate": {"en": "thiopropazate", "zh": "硫普拉嗪", "factor": 5},
        "thioproperazine": {"en": "thioproperazine", "zh": "硫普拉嗪", "factor": 4},
        "thioridazine": {"en": "thioridazine", "zh": "硫利达嗪", "factor": 1},
        "tiapride": {"en": "tiapride", "zh": "硫必利", "factor": 0.75},
        "tiospene": {"en": "tiospene", "zh": "噻奥司平", "factor": 10},
        "trifluoperazine": {"en": "trifluoperazine", "zh": "三氟拉嗪", "factor": 15},
        "trifluperidol": {"en": "trifluperidol", "zh": "三氟哌利多", "factor": 150},
        "triflupromazine": {"en": "triflupromazine", "zh": "三氟拉嗪", "factor": 3},
        "ziprasidone": {"en": "ziprasidone", "zh": "齐拉西酮", "factor": 3.75},
        "zotepine": {"en": "zotepine", "zh": "唑替平", "factor": 1.5},
        "zuclopenthixol": {"en": "zuclopenthixol", "zh": "舒氯苯噻吨", "factor": 10}
    }

    # 创建反向查找字典
    name_to_key = {}
    for key, value in antipsychotics.items():
        name_to_key[value['en'].lower()] = key
        name_to_key[value['zh']] = key

    drug = drug.lower()
    if drug in name_to_key:
        key = name_to_key[drug]
        return dose * antipsychotics[key]['factor']
    else:
        return "未知药物或尚未收录在数据库中"

# 定义GUI程序
def calculate():
    drug_name = drug_name_entry.get()
    try:
        drug_dose = float(drug_dose_entry.get())
    except ValueError:
        messagebox.showerror("输入错误", "无效的剂量输入，请输入一个数字。")
        return
    
    result = calculate_chlorpromazine_equivalent(drug_name, drug_dose)
    if isinstance(result, (int, float)):
        result_label.config(text=f"{drug_name} {drug_dose}mg/d 的氯丙嗪当量为 {result}mg/d")
    else:
        result_label.config(text=result)

# 创建主窗口
root = tk.Tk()
root.title("抗精神病药氯丙嗪当量计算器")

# 创建并放置组件
tk.Label(root, text="抗精神病药名称（中文或英文）:").grid(row=0, column=0, padx=10, pady=5)
drug_name_entry = tk.Entry(root)
drug_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="药物剂量 (mg/d):").grid(row=1, column=0, padx=10, pady=5)
drug_dose_entry = tk.Entry(root)
drug_dose_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="计算", command=calculate)
calculate_button.grid(row=2, columnspan=2, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2, pady=5)

# 运行主循环
root.mainloop()
