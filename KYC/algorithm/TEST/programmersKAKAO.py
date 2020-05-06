# from bs4 import BeautifulSoup

# def solution(word,pages):
#     # 기본점수, 외부링크 수, 링크 사이트
#     site_dic = {}
#     word = word.upper()

#     for page in pages:
#         soup = BeautifulSoup(page,"html.parser")
        
#         site = soup.select("meta + meta")
#         site = site[0].get("content")
#         site_dic[site] = [0,0,[]]

#         content = soup.find("body")
#         link = content.select("a")
#         for body_text in content:
#             if len(body_text) == 0:
#                 break
#             else:
#                 for i in range(len(word),len(body_text)):
#                     check_word = body_text[i-len(word):i]
#                     check_word = check_word.upper()
#                     if check_word == word:
#                         site_dic[site][0] += 1
        
#         for l in link:
#             site_dic[site][2].append(l.get("href"))
#             site_dic[site][1] += 1
    
#     result = 0
#     r_index = 0
#     ind = -1
#     for site in site_dic:
#         ind += 1
#         link_point = 0
#         for link in site_dic[site][2]:
#             if link in site_dic.keys():
#                 link_point += site_dic[link][0]
#         point = site_dic[site][0] + link_point / site_dic[site][1]
#         if point > result:
#             result = point
#             r_index = ind
    
#     return r_index


def solution(word,pages):
    # 기본점수, 외부링크 수, 링크 사이트
    site_dic = {}
    word = word.upper()
    for page in pages:
        all_content = page.strip("\n").splitlines()
        body_check = False
        site = ""
        for row in all_content:
            row = row.strip()
            if row[:len('<meta ')] == '<meta ':
                new_row = row.split("content=")

                if len(new_row) > 1:
                    site = new_row[1][: len(new_row[1])-2]
                    site_dic[site] = [0,0,[],0]
            elif row == "<body>":
                body_check =True

            elif body_check == True:
                content_row = row.split("</a>")
                for content in content_row:
                    content = content.split("<a ")
                    for cont in content:
                        end = 0
                        if cont[:4] =="href":
                            
                            for s in range(3,len(cont)):
                                if cont[s] == ">":
                                    end = s
                                    break
                        
                            site_dic[site][2].append(cont[5:end])
                            site_dic[site][1] += 1
                        
                        word_check = cont[end:]
                        change_word = ""
                        for ind in range(len(word_check)):
                            add = word_check[ind]
                            if word_check[ind].isalpha() == False:
                                add = " "
                            change_word += add
                        
                        change_word = change_word.split()

                        for c_word in change_word:
                            c_word = c_word.upper()
                            if word == c_word:
                                site_dic[site][0] += 1
                    
            elif row == "</body>":
                break
    
    
    for site in site_dic:
        for link in site_dic[site][2]:
            if link in site_dic.keys():
                site_dic[link][3] += (site_dic[site][0] / site_dic[site][1])
    
    max = 0
    r_index = 0
    index = -1

    for site in site_dic:
        index += 1
        if max < site_dic[site][0] + site_dic[site][3]:
            max = site_dic[site][0] + site_dic[site][3]
            r_index = index
    
    return r_index








a = ["<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://a.com\"/>\n</head>  \n<body>\nBlind Lorem Blind ipsum dolor Blind test sit amet, consectetur adipiscing elit. \n<a href=\"https://b.com\"> Link to b </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://b.com\"/>\n</head>  \n<body>\nSuspendisse potenti. Vivamus venenatis tellus non turpis bibendum, \n<a href=\"https://a.com\"> Link to a </a>\nblind sed congue urna varius. Suspendisse feugiat nisl ligula, quis malesuada felis hendrerit ut.\n<a href=\"https://c.com\"> Link to c </a>\n</body>\n</html>", "<html lang=\"ko\" xml:lang=\"ko\" xmlns=\"http://www.w3.org/1999/xhtml\">\n<head>\n  <meta charset=\"utf-8\">\n  <meta property=\"og:url\" content=\"https://c.com\"/>\n</head>  \n<body>\nUt condimentum urna at felis sodales rutrum. Sed dapibus cursus diam, non interdum nulla tempor nec. Phasellus rutrum enim at orci consectetu blind\n<a href=\"https://a.com\"> Link to a </a>\n</body>\n</html>"]
print(solution("blind",a))
