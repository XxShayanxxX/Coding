#Program for KMP Algorithm 
def KMPpattern(pat,text):
    M = len(pat)
    N = len(text)


    #create ips[] that will hold the longest prefix suffix
    #values for pattern

    lps = [0]*M #index for pat[]
    j = 0

    #Preprocess the pattern calculate Ips[] array)

    LPSArray(pat,M,lps)

    i = 0 
    while(N - i) >= (M - j):
        if pat[j] == text[i]:
            i += 1 
            j += 1 

         if j == M:
            print ("Found pattern at index " + str(i-j))
            j = lps[j-1]

        #mismatch afyer j matches 
        elif i < N and pat[j] != text[i]:
            #Do not match lps characters,
            #they will match anyway 

            if j != 0:
                j = lps[j-1]

            else:
                i += 1 

def LPSArray(pat,M,lps):
    len = 0 #len of the prebious prefixz suffix 

    lps[0]
    i = 1 

    #the loop calculates lps[i] for i = 1 to M-1 
    while i < M:
        if pat[i] == pat[len]:
            len += 1 
            lps[i] = len
            i += 1

        else:
            if len != 0:
                len = lps[len-1]

                #Also note that we don not increment i here

            else:
                lps[i] = 0 
                i += 1 


text = "ABCDDCANDCDABABDDA"
pat = "DABA"
KMPpattern(pat,text)