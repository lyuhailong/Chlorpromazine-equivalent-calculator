import tkinter as tk
from tkinter import messagebox

# 药物信息字典
antipsychotics = {
    "acepromazine": {"en": "acepromazine", "zh": "乙酰普罗马嗪", "chlorpromazine_factor": 3, "olanzapine_factor": 0.1},
    "acetophenazine": {"en": "acetophenazine", "zh": "乙酰苯哌嗪", "chlorpromazine_factor": 6, "olanzapine_factor": 0.2},
    "amisulpride": {"en": "amisulpride", "zh": "氨磺必利", "chlorpromazine_factor": 0.75, "olanzapine_factor": 0.03},
    "aripiprazole": {"en": "aripiprazole", "zh": "阿立哌唑", "chlorpromazine_factor": 20, "olanzapine_factor": 0.67},
    "asenapine": {"en": "asenapine", "zh": "阿塞那平", "chlorpromazine_factor": 15, "olanzapine_factor": 0.5},
    "benperidol": {"en": "benperidol", "zh": "苯哌利多", "chlorpromazine_factor": 200, "olanzapine_factor": 6.67},
    "bromperidol": {"en": "bromperidol", "zh": "溴哌利多", "chlorpromazine_factor": 30, "olanzapine_factor": 1},
    "cariprazine": {"en": "cariprazine", "zh": "卡立普嗪", "chlorpromazine_factor": 30, "olanzapine_factor": 1},
    "chlorpromazine": {"en": "chlorpromazine", "zh": "氯丙嗪", "chlorpromazine_factor": 1, "olanzapine_factor": 0.03},
    "chlorprothixene": {"en": "chlorprothixene", "zh": "氯丙噻吨", "chlorpromazine_factor": 1, "olanzapine_factor": 0.03},
    "clopenthixol": {"en": "clopenthixol", "zh": "氯喷噻吨", "chlorpromazine_factor": 3, "olanzapine_factor": 0.1},
    "clotiapine": {"en": "clotiapine", "zh": "氯噻平", "chlorpromazine_factor": 3.75, "olanzapine_factor": 0.13},
    "clozapine": {"en": "clozapine", "zh": "氯氮平", "chlorpromazine_factor": 1, "olanzapine_factor": 0.03},
    "flupentixol": {"en": "flupentixol", "zh": "氟哌噻吨", "chlorpromazine_factor": 50, "olanzapine_factor": 1.67},
    "fluphenazine": {"en": "fluphenazine", "zh": "氟奋乃静", "chlorpromazine_factor": 30, "olanzapine_factor": 1},
    "haloperidol": {"en": "haloperidol", "zh": "氟哌啶醇", "chlorpromazine_factor": 37.5, "olanzapine_factor": 1.25},
    "levomepromazine": {"en": "levomepromazine", "zh": "左美普嗪", "chlorpromazine_factor": 1, "olanzapine_factor": 0.03},
    "loxapine": {"en": "loxapine", "zh": "洛沙平", "chlorpromazine_factor": 3, "olanzapine_factor": 0.1},
    "lurasidone": {"en": "lurasidone", "zh": "鲁拉西酮", "chlorpromazine_factor": 5, "olanzapine_factor": 0.17},
    "melperone": {"en": "melperone", "zh": "美普仑", "chlorpromazine_factor": 1, "olanzapine_factor": 0.03},
    "mesoridazine": {"en": "mesoridazine", "zh": "美索达嗪", "chlorpromazine_factor": 1.5, "olanzapine_factor": 0.05},
    "molindone": {"en": "molindone", "zh": "莫林酮", "chlorpromazine_factor": 6, "olanzapine_factor": 0.2},
    "moperone": {"en": "moperone", "zh": "吗哌隆", "chlorpromazine_factor": 15, "olanzapine_factor": 0.5},
    "olanzapine": {"en": "olanzapine", "zh": "奥氮平", "chlorpromazine_factor": 30, "olanzapine_factor": 1},
    "oxypertine": {"en": "oxypertine", "zh": "奥克舍平", "chlorpromazine_factor": 2.5, "olanzapine_factor": 0.08},
    "paliperidone": {"en": "paliperidone", "zh": "帕利哌酮", "chlorpromazine_factor": 50, "olanzapine_factor": 1.67},
    "penfluridol": {"en": "penfluridol", "zh": "喷氟利多", "chlorpromazine_factor": 50, "olanzapine_factor": 1.67},
    "perazine": {"en": "perazine", "zh": "哌拉嗪", "chlorpromazine_factor": 3, "olanzapine_factor": 0.1},
    "periciazine": {"en": "periciazine", "zh": "哌氯嗪", "chlorpromazine_factor": 6, "olanzapine_factor": 0.2},
    "perphenazine": {"en": "perphenazine", "zh": "奋乃静", "chlorpromazine_factor": 10, "olanzapine_factor": 0.33},
    "pimozide": {"en": "pimozide", "zh": "匹莫齐特", "chlorpromazine_factor": 75, "olanzapine_factor": 2.5},
    "pipamperone": {"en": "pipamperone", "zh": "匹帕佩隆", "chlorpromazine_factor": 1.5, "olanzapine_factor": 0.05},
    "pipotiazine": {"en": "pipotiazine", "zh": "匹泊噻嗪", "chlorpromazine_factor": 30, "olanzapine_factor": 1},
    "prochlorperazine": {"en": "prochlorperazine", "zh": "普鲁氯嗪", "chlorpromazine_factor": 3, "olanzapine_factor": 0.1},
    "promazine": {"en": "promazine", "zh": "异丙嗪", "chlorpromazine_factor": 1, "olanzapine_factor": 0.03},
    "prothipendyl": {"en": "prothipendyl", "zh": "普罗噻吡", "chlorpromazine_factor": 1.25, "olanzapine_factor": 0.04},
    "quetiapine": {"en": "quetiapine", "zh": "喹硫平", "chlorpromazine_factor": 0.75, "olanzapine_factor": 0.03},
    "remoxipride": {"en": "remoxipride", "zh": "瑞莫西利", "chlorpromazine_factor": 1, "olanzapine_factor": 0.03},
    "risperidone": {"en": "risperidone", "zh": "利培酮", "chlorpromazine_factor": 60, "olanzapine_factor": 2},
    "sertindole": {"en": "sertindole", "zh": "舍萘酮", "chlorpromazine_factor": 18.75, "olanzapine_factor": 0.63},
    "sulpiride": {"en": "sulpiride", "zh": "舒必利", "chlorpromazine_factor": 0.375, "olanzapine_factor": 0.01},
    "sultopiride": {"en": "sultopiride", "zh": "舒托必利", "chlorpromazine_factor": 0.25, "olanzapine_factor": 0.01},
    "thiopropazate": {"en": "thiopropazate", "zh": "硫丙嗪", "chlorpromazine_factor": 5, "olanzapine_factor": 0.17},
    "thioproperazine": {"en": "thioproperazine", "zh": "硫丙拉嗪", "chlorpromazine_factor": 4, "olanzapine_factor": 0.13},
    "thioridazine": {"en": "thioridazine", "zh": "硫利达嗪", "chlorpromazine_factor": 1, "olanzapine_factor": 0.03},
    "tiapride": {"en": "tiapride", "zh": "硫必利", "chlorpromazine_factor": 0.75, "olanzapine_factor": 0.03},
    "tiospene": {"en": "tiospene", "zh": "噻奥司平", "chlorpromazine_factor": 10, "olanzapine_factor": 0.33},
    "trifluoperazine": {"en": "trifluoperazine", "zh": "三氟拉嗪", "chlorpromazine_factor": 15, "olanzapine_factor": 0.5},
    "trifluperidol": {"en": "trifluperidol", "zh": "三氟哌利多", "chlorpromazine_factor": 150, "olanzapine_factor": 5},
    "triflupromazine": {"en": "triflupromazine", "zh": "三氟拉嗪", "chlorpromazine_factor": 3, "olanzapine_factor": 0.1},
    "ziprasidone": {"en": "ziprasidone", "zh": "齐拉西酮", "chlorpromazine_factor": 3.75, "olanzapine_factor": 0.13},
    "zotepine": {"en": "zotepine", "zh": "唑替平", "chlorpromazine_factor": 1.5, "olanzapine_factor": 0.05},
    "zuclopenthixol": {"en": "zuclopenthixol", "zh": "舒氯苯噻吨", "chlorpromazine_factor": 10, "olanzapine_factor": 0.33},
    "aripiprazole_lai4": {"en": "Aripiprazole LAI4", "zh": "阿立哌唑4周", "chlorpromazine_factor": 27.52, "olanzapine_factor": 0.92},
    "olanzapine_lai4": {"en": "Olanzapine LAI4", "zh": "奥氮平4周", "chlorpromazine_factor": 22.90, "olanzapine_factor": 0.76},
    "paliperidone_lai4": {"en": "Paliperidone LAI4", "zh": "帕利哌酮4周", "chlorpromazine_factor": 47.62, "olanzapine_factor": 1.59},
    "paliperidone_lai2": {"en": "Paliperidone LAI2", "zh": "利培酮2周", "chlorpromazine_factor": 176.47, "olanzapine_factor": 5.88}
}

# 创建反向查找字典
name_to_key = {}
for key, value in antipsychotics.items():
    name_to_key[value['en'].lower()] = key
    name_to_key[value['zh']] = key

def calculate_equivalent(drug, dose):
    drug = drug.lower()
    if drug in name_to_key:
        key = name_to_key[drug]
        chlorpromazine_equivalent = dose * antipsychotics[key]['chlorpromazine_factor']
        olanzapine_equivalent = dose * antipsychotics[key]['olanzapine_factor']
        return chlorpromazine_equivalent, olanzapine_equivalent
    else:
        return "未知药物或尚未收录在数据库中", "未知药物或尚未收录在数据库中"

# 定义GUI程序
def calculate():
    drug_name = drug_name_entry.get()
    try:
        drug_dose = float(drug_dose_entry.get())
    except ValueError:
        messagebox.showerror("输入错误", "无效的剂量输入，请输入一个数字。")
        return
    
    chlorpromazine_result, olanzapine_result = calculate_equivalent(drug_name, drug_dose)
    
    if isinstance(chlorpromazine_result, (int, float)) and isinstance(olanzapine_result, (int, float)):
        result_label.config(text=f"{drug_name} {drug_dose}mg/d 的氯丙嗪当量为 {chlorpromazine_result:.2f}mg/d\n"
                                 f"{drug_name} {drug_dose}mg/d 的奥氮平当量为 {olanzapine_result:.2f}mg/d")
    else:
        result_label.config(text=chlorpromazine_result)

# 创建主窗口
root = tk.Tk()
root.title("抗精神病药等效剂量计算器")

# 创建并放置组件
tk.Label(root, text="抗精神病药名称（中文或英文）:").grid(row=0, column=0, padx=10, pady=5)
drug_name_entry = tk.Entry(root)
drug_name_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="药物剂量 (mg/d):").grid(row=1, column=0, padx=10, pady=5)
drug_dose_entry = tk.Entry(root)
drug_dose_entry.grid(row=1, column=1, padx=10, pady=5)

calculate_button = tk.Button(root, text="计算", command=calculate)
calculate_button.grid(row=2, columnspan=2, pady=10)

result_label = tk.Label(root, text="", justify=tk.LEFT)
result_label.grid(row=3, columnspan=2, pady=5)

# 运行主循环
root.mainloop()
