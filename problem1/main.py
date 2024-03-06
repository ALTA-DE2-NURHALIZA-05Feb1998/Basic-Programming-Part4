def play_with_asterisk(N):
    pattern=''
    for i in range (N):
        for j in range(N - i - 1):
            pattern += ' '
        for j in range(i + 1):
            pattern += '* '
        pattern += '\n'
    return pattern
if __name__ == '__main__':
    print(play_with_asterisk(5))
    """
        *
       * *
      * * *
     * * * *
    * * * * *
    """