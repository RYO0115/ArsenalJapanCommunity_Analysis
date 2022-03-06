
def CountUpItems(df, label):
    sizes = [0 for i in range(len(label)+1)]

    for row in df:

        counted = 0
        for i in range(len(label)):
            if row.find(label[i]) != -1:
                sizes[i] = sizes[i] + 1
                counted = counted + 1
        if counted == 0:
            sizes[-1] = sizes[-1] + 1

    return(sizes)


def CoutUpSupportingYears(df):
    label_jp = ["10年以上","3~10年", "1~3年", "見始めたばかり", ]
    label = [" > 10years","3 ~ 10 years", "1 ~ 3 years", " < 1year"]
    sizes = CountUpItems(df, label_jp)

    return(label, sizes[:-1])
