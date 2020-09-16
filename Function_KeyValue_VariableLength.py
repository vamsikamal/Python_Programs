def disp(**kw):
    print(type(kw))
    for k,v in kw.items():
        print(k, v)


disp(a=10, b=20, c= 30)
disp(name1 = "SLC", name2="Python", name3="Hyd", name4="Programming")