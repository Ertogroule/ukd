#rating1 is Player's rating, rating2 is Opponent's rating, result is the result of the match. 1=Win 0.5=Draw 0=Lose

def ukdchange(rating1, rating2, result):
    error = 'Please enter valid numbers'
    
    if 0 > (int(rating1) and int(rating2)):
        return error
    if not result in [0, 0.5, 1]:
        return error
    if 0 < (int(rating1) or int(rating2)) < 1000:
        return error
    if rating1 == 0:
        return error
    #This function can not calculate ukd change if Player doesn't have an ukd rating, as you would need to know the ukd ratings of all players in the tournament.

    if (rating1 or rating2) > 9999:
        return error
    expected_score = 0
    k1 = k2 = 30
    #k means coefficient

    if rating1 > 1299:
        k1 = 25
        if rating1 > 1599:
            k1 = 20
            if rating1 > 1999:
                k1 = 15
                if rating1 > 2399:
                    k1 = 10 

    if rating2 > 1299:
        k2 = 25
        if rating2 > 1599:
            k2 = 20
            if rating2 > 1999:
                k2 = 15
                if rating2 > 2399:
                    k2 = 10 
    
    dif = abs(rating1 - rating2)
    es = 50 #es means expected score. dif means rating difference. This long if statement code below is the system used to calculate expected score according to rating difference.
    if dif > 3:
        es = 51
        if dif > 10:
            es = 52
            if dif > 17:
                es = 53
                if dif > 25:
                    es = 54
                    if dif > 32:
                        es = 55
                        if dif > 39:
                            es = 56
                            if dif > 46:
                                es = 57
                                if dif > 53:
                                    es = 58
                                    if dif > 61:
                                        es = 59
                                        if dif > 68:
                                            es = 60 
                                            if dif > 76:
                                                es = 61
                                                if dif > 83:
                                                    es = 62
                                                    if dif > 91:
                                                        es = 63
                                                        if dif > 98:
                                                            es = 64
                                                            if dif > 106:
                                                                es = 65
                                                                if dif > 113:
                                                                    es = 66
                                                                    if dif > 121:
                                                                        es = 67
                                                                        if dif > 129:
                                                                            es = 68
                                                                            if dif > 137:
                                                                                es = 69
                                                                                if dif > 145:
                                                                                    es = 70
                                                                                    if dif > 153:
                                                                                        es = 71
                                                                                        if dif > 162:
                                                                                            es = 72
                                                                                            if dif > 170:
                                                                                                es = 73
                                                                                                if dif >179:
                                                                                                    es = 74
                                                                                                    if dif > 188:
                                                                                                        es = 75
                                                                                                        if dif > 197:
                                                                                                            es = 76
                                                                                                            if dif > 206:
                                                                                                                es = 77
                                                                                                                if dif > 215:
                                                                                                                    es = 78
                                                                                                                    if dif > 225:
                                                                                                                        es = 79
                                                                                                                        if dif > 235:
                                                                                                                            es = 80
                                                                                                                            if dif > 245:
                                                                                                                                es = 81
                                                                                                                                if dif > 256:
                                                                                                                                    es = 82
                                                                                                                                    if dif > 267:
                                                                                                                                        es = 83 
                                                                                                                                        if dif > 278:
                                                                                                                                            es = 84
                                                                                                                                            if dif > 290:
                                                                                                                                                es = 85
                                                                                                                                                if dif > 302:
                                                                                                                                                    es = 86
                                                                                                                                                    if dif > 315:
                                                                                                                                                        es = 87
                                                                                                                                                        if dif > 328:
                                                                                                                                                            es = 88
                                                                                                                                                            if dif > 344:
                                                                                                                                                                es = 89
    if rating1 > rating2:
        expected_score = es / 100
    else:
        expected_score = (100 - es) / 100
               
    rating_change1 = k1 * (result - expected_score)
    rating_change2 = k2 * (-result +expected_score)

    if rating2 == 0:
        rating_change2 = 0
        if result == 1:
            rating_change1 = k1 * 1 / 10
        elif result == 0.5:
            rating_change1 = 0
        else:
            rating_change1 = k1 * -1 / 10

    r1=rating1

    rating1 += rating_change1
    rating2 += rating_change2

    if rating1 < 1000:
        rating_change1=r1-1000
        rating1 = 1000

    if rating2 < 1000:
        rating2 = 1000
    
    rating_change1= round(rating_change1, 1)
    rating1= round(rating1,1)
    rating2=round(rating2,1)

    return rating1, rating2

#print(ukdchange(1303,1200,1))
