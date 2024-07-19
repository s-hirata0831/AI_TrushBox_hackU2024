import csv
import random as rnd

#------
#初期化用プログラム
#------
def resetCsv():
    #譜面二次配列
    l = [[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0]]
    #本数保持配列
    n = [[0, 0]]
    #譜面初期化
    with open('fishSave/state.csv', 'w') as f:
        writer = csv.writer(f)
        writer.writerows(l)
    #本数初期化
    with open('fishSave/checkNum.csv', 'w') as num:
        write = csv.writer(num)
        write.writerows(n)

#------
#本数更新用
#------
def writeNum(cNum, pNum):
    with open('fishSave/checkNum.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    can = rows[0][0]
    pet = rows[0][1]
    if int(can) != int(cNum) or int(pet) != int(pNum):
        judgeCan = int(can) % 2
        judgePet = int(pet) % 2
        print(judgeCan)
        print(judgePet)
        if judgeCan == 0:
            can = cNum
            with open('fishSave/checkNum', 'w') as r:
                write = csv.writer(r)
                write.writerows(can)
            return True
        elif judgePet == 0:
            pet = pNum
            with open('fishSave/checkNum', 'w') as p:
                write = csv.writer(p)
                write.writerows(pet)
            return True
        else:
            return 1
    else:
        print("新たにゴミは投入されませんでした。")
        return False
    
#------
#譜面ランダム割り当て
#------
def random(cNum, pNum):
    canNum = int(cNum) % 2
    petNum = int(pNum) % 2
    if canNum == 0:
        trueTag = int(cNum) / 2
        with open("fishSave/state.csv", 'r') as rf:
            reader = csv.reader(rf)
            rows = list(reader)
        trustTag = 0
        #譜面の現状
        if int(rows[0][0]) == 1 or int(rows[0][0]) == 2:
            trustTag += 1
        if int(rows[0][2]) == 1 or int(rows[0][2]) == 2:
            trustTag += 1
        if int(rows[0][4]) == 1 or int(rows[0][4]) == 2:
            trustTag += 1
        if int(rows[0][6]) == 1 or int(rows[0][6]) == 2:
            trustTag += 1
        if int(rows[0][8]) == 1 or int(rows[0][8]) == 2:
            trustTag += 1
        if int(rows[1][1]) == 1 or int(rows[1][1]) == 2:
            trustTag += 1
        if int(rows[1][3]) == 1 or int(rows[1][3]) == 2:
            trustTag += 1
        if int(rows[1][5]) == 1 or int(rows[1][5]) == 2:
            trustTag += 1
        if int(rows[1][7]) == 1 or int(rows[1][7]) == 2:
            trustTag += 1
        if int(rows[1][9]) == 1 or int(rows[1][9]) == 2:
            trustTag += 1
        if int(rows[2][0]) == 1 or int(rows[2][0]) == 2:
            trustTag += 1
        if int(rows[2][2]) == 1 or int(rows[2][2]) == 2:
            trustTag += 1
        if int(rows[2][4]) == 1 or int(rows[2][4]) == 2:
            trustTag += 1
        if int(rows[2][6]) == 1 or int(rows[2][6]) == 2:
            trustTag += 1
        if int(rows[2][8]) == 1 or int(rows[2][8]) == 2:
            trustTag += 1
        #新たに生成すべきコマの数を計算
        if int(trustTag) < int(trueTag):
            genTag = int(trueTag) - int(trustTag)
        #要素をナンバリング
        c1 = rows[0][0]
        c2 = rows[0][2]
        c3 = rows[0][4]
        c4 = rows[0][6]
        c5 = rows[0][8]
        c6 = rows[1][1]
        c7 = rows[1][3]
        c8 = rows[1][5]
        c9 = rows[1][7]
        c10 = rows[1][9]
        c11 = rows[2][0]
        c12 = rows[2][2]
        c13 = rows[2][4]
        c14 = rows[2][6]
        c15 = rows[2][8]
        value = [c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12, c13, c14, c15]
        for i in range(genTag):
            key = random.randint(1,15)
            tag = value[int(key) - 1]
            if int(tag) == 0:
                print("tagを1に変更")
                tag = 1
                with open("fishSave/state.csv", 'w') as wf:
                    write = csv.writer(wf)
                    write.writerows(tag)


# BOMを除去するための関数
def remove_bom(line):
    BOM = '\ufeff'
    if line.startswith(BOM):
        return line[1:]
    else:
        return line

# 譜面ランダム割り当て
def randomScr(cNum, pNum):
    canNum = int(cNum) % 2
    petNum = int(pNum) % 2
    if canNum == 0:
        trueTag = int(cNum) / 2
        with open("fishSave/state.csv", 'r', encoding='utf-8') as rf:
            reader = csv.reader(rf)
            rows = [remove_bom(row) for row in rf]  # BOMを除去
            rows = list(csv.reader(rows))
        trustTag = 0
        
        # 譜面の現状
        target_positions = [(0, 0), (0, 2), (0, 4), (0, 6), (0, 8), 
                            (1, 1), (1, 3), (1, 5), (1, 7), (1, 9), 
                            (2, 0), (2, 2), (2, 4), (2, 6), (2, 8)]
        
        for r, c in target_positions:
            if int(rows[r][c]) == 1 or int(rows[r][c]) == 2:
                trustTag += 1
        
        # 新たに生成すべきコマの数を計算
        if int(trustTag) < int(trueTag):
            genTag = int(trueTag) - int(trustTag)
        
        # 要素をナンバリング
        value = [rows[r][c] for r, c in target_positions]
        
        for _ in range(genTag):
            while True:
                key = rnd.randint(0, 14)  # rnd.randintを使用
                if int(value[key]) == 0:
                    value[key] = 1
                    break
        
        # 更新した要素を元の行列に戻す
        for i, (r, c) in enumerate(target_positions):
            rows[r][c] = value[i]
        
        # 更新した行列をcsvファイルに書き戻す
        with open("fishSave/state.csv", 'w', newline='', encoding='utf-8') as wf:
            writer = csv.writer(wf)
            writer.writerows(rows)
        
    if petNum == 0:
        trueTag = int(pNum) / 2
        with open("fishSave/state.csv", 'r', encoding='utf-8') as rf:
            reader = csv.reader(rf)
            rows = [remove_bom(row) for row in rf]  # BOMを除去
            rows = list(csv.reader(rows))
        trustTag = 0
        
        # 譜面の現状
        target_positions = [(0, 1), (0, 3), (0, 5), (0, 7), (0, 9), 
                            (1, 0), (1, 2), (1, 4), (1, 6), (1, 8), 
                            (2, 1), (2, 3), (2, 5), (2, 7), (2, 9)]
        
        for r, c in target_positions:
            if int(rows[r][c]) == 1 or int(rows[r][c]) == 2:
                trustTag += 1
        
        # 新たに生成すべきコマの数を計算
        if int(trustTag) < int(trueTag):
            genTag = int(trueTag) - int(trustTag)
        
        # 要素をナンバリング
        value = [rows[r][c] for r, c in target_positions]
        
        for _ in range(genTag):
            while True:
                key = rnd.randint(0, 14)  # rnd.randintを使用
                if int(value[key]) == 0:
                    value[key] = 1
                    break
        
        # 更新した要素を元の行列に戻す
        for i, (r, c) in enumerate(target_positions):
            rows[r][c] = value[i]
        
        # 更新した行列をcsvファイルに書き戻す
        with open("fishSave/state.csv", 'w', newline='', encoding='utf-8') as wf:
            writer = csv.writer(wf)
            writer.writerows(rows)

    update_column_if_all_one("fishSave/state.csv")

def update_column_if_all_one(file_path):
    # CSVファイルからデータを読み込む
    with open(file_path, 'r', encoding='utf-8-sig') as rf:
        reader = csv.reader(rf)
        rows = list(reader)
    
    # 各列についてチェックし、全ての値が1であれば2に変更
    for c in range(10):  # 10列すべてチェック
        all_one = True
        for r in range(3):
            if int(rows[r][c]) != 1:
                all_one = False
                break
        if all_one:
            for r in range(3):
                rows[r][c] = '2'
    
    # 更新されたデータをCSVファイルに書き戻す
    with open(file_path, 'w', newline='', encoding='utf-8-sig') as wf:
        writer = csv.writer(wf)
        writer.writerows(rows)

def readCsv(r,c):
    with open('fishSave/state.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    value = rows[r][c]
    return value

def checkNum(can, pet):
    with open('fishSave/checkNum.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    
    cNum = rows[0][0]
    pNum = rows[0][1]

    #缶とペットボトルの数が更新されているか確認
    if cNum != can or pNum != pet:
        writeNum(can)
        writeNum
        return True

#要素を確認して書き込む    
def test():
    with open('fishSave/checkNum.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)

    cNum = rows[0][0]
    if cNum != str(0):
        print("CNumは0です。")
        rows[0][0] = 0
        with open('fishSave/checkNum.csv', 'w') as fi:
            writer = csv.writer(fi)
            writer.writerows(rows)
    else:
        print("1以外")

resetCsv()