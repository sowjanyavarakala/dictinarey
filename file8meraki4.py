 f=open("main.txt",'r')
 k=f.readlines()
 for i in k:
         if "delhi" in i:
                     b=open("maindelhi.txt","a")
                             b.write (i)
                                      print(b)
                                           elif "shimla" in i:
                                                       p=open("mainshimla.txt","a")
                                                               p.write(i)
                                                                       print(p)
                                                                           else:
                                                                                s=open("mainothers.txt","a")
                                                                                    s.write(i)
                                                                                        print(s)