def ft_atoi(str):
    i = 0
    sign = 1
    result = 0
    while str[i:] and (str[i] == ' ' or str[i] == '\t' or str[i] == '\n' or str[i] == '\v' or str[i] == '\f'):
        i += 1
    if str[i:] and (str[i] == '-' or str[i] == '+'):
        sign = -1 if str[i] == '-' else 1
        i += 1
    while str[i:] and '0' <= str[i] <= '9':
        result = result * 10 + int(str[i])
        i += 1
    return sign * result
