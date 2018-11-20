import calendar


def semester_calendar(output_type, year, first_month, last_month):
    """
    (str, int, int) -> None

    >>> semester_calendar("html", 2016, 2, 3)
    <table border="0" cellpadding="0" cellspacing="0" class="month">
    <tr><th colspan="7" class="month">February 2016</th></tr>
    <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
    <tr><td class="mon">1</td><td class="tue">2</td><td class="wed">3</td><td class="thu">4</td><td class="fri">5</td><td class="sat">6</td><td class="sun">7</td></tr>
    <tr><td class="mon">8</td><td class="tue">9</td><td class="wed">10</td><td class="thu">11</td><td class="fri">12</td><td class="sat">13</td><td class="sun">14</td></tr>
    <tr><td class="mon">15</td><td class="tue">16</td><td class="wed">17</td><td class="thu">18</td><td class="fri">19</td><td class="sat">20</td><td class="sun">21</td></tr>
    <tr><td class="mon">22</td><td class="tue">23</td><td class="wed">24</td><td class="thu">25</td><td class="fri">26</td><td class="sat">27</td><td class="sun">28</td></tr>
    <tr><td class="mon">29</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
    </table>
    <BLANKLINE>
    <table border="0" cellpadding="0" cellspacing="0" class="month">
    <tr><th colspan="7" class="month">March 2016</th></tr>
    <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
    <tr><td class="noday">&nbsp;</td><td class="tue">1</td><td class="wed">2</td><td class="thu">3</td><td class="fri">4</td><td class="sat">5</td><td class="sun">6</td></tr>
    <tr><td class="mon">7</td><td class="tue">8</td><td class="wed">9</td><td class="thu">10</td><td class="fri">11</td><td class="sat">12</td><td class="sun">13</td></tr>
    <tr><td class="mon">14</td><td class="tue">15</td><td class="wed">16</td><td class="thu">17</td><td class="fri">18</td><td class="sat">19</td><td class="sun">20</td></tr>
    <tr><td class="mon">21</td><td class="tue">22</td><td class="wed">23</td><td class="thu">24</td><td class="fri">25</td><td class="sat">26</td><td class="sun">27</td></tr>
    <tr><td class="mon">28</td><td class="tue">29</td><td class="wed">30</td><td class="thu">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
    </table>
    <BLANKLINE>
    >>> semester_calendar("txt", 2016, 2, 3)
       February 2016
    Mo Tu We Th Fr Sa Su
     1  2  3  4  5  6  7
     8  9 10 11 12 13 14
    15 16 17 18 19 20 21
    22 23 24 25 26 27 28
    29
    <BLANKLINE>
         March 2016
    Mo Tu We Th Fr Sa Su
        1  2  3  4  5  6
     7  8  9 10 11 12 13
    14 15 16 17 18 19 20
    21 22 23 24 25 26 27
    28 29 30 31
    <BLANKLINE>
    >>> semester_calendar("txt", 2020, 2, 3)
       February 2020
    Mo Tu We Th Fr Sa Su
                    1  2
     3  4  5  6  7  8  9
    10 11 12 13 14 15 16
    17 18 19 20 21 22 23
    24 25 26 27 28 29
    <BLANKLINE>
         March 2020
    Mo Tu We Th Fr Sa Su
                       1
     2  3  4  5  6  7  8
     9 10 11 12 13 14 15
    16 17 18 19 20 21 22
    23 24 25 26 27 28 29
    30 31
    <BLANKLINE>
    >>> semester_calendar("html", 2020, 2, 3)
    <table border="0" cellpadding="0" cellspacing="0" class="month">
    <tr><th colspan="7" class="month">February 2020</th></tr>
    <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
    <tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="sat">1</td><td class="sun">2</td></tr>
    <tr><td class="mon">3</td><td class="tue">4</td><td class="wed">5</td><td class="thu">6</td><td class="fri">7</td><td class="sat">8</td><td class="sun">9</td></tr>
    <tr><td class="mon">10</td><td class="tue">11</td><td class="wed">12</td><td class="thu">13</td><td class="fri">14</td><td class="sat">15</td><td class="sun">16</td></tr>
    <tr><td class="mon">17</td><td class="tue">18</td><td class="wed">19</td><td class="thu">20</td><td class="fri">21</td><td class="sat">22</td><td class="sun">23</td></tr>
    <tr><td class="mon">24</td><td class="tue">25</td><td class="wed">26</td><td class="thu">27</td><td class="fri">28</td><td class="sat">29</td><td class="noday">&nbsp;</td></tr>
    </table>
    <BLANKLINE>
    <table border="0" cellpadding="0" cellspacing="0" class="month">
    <tr><th colspan="7" class="month">March 2020</th></tr>
    <tr><th class="mon">Mon</th><th class="tue">Tue</th><th class="wed">Wed</th><th class="thu">Thu</th><th class="fri">Fri</th><th class="sat">Sat</th><th class="sun">Sun</th></tr>
    <tr><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="sun">1</td></tr>
    <tr><td class="mon">2</td><td class="tue">3</td><td class="wed">4</td><td class="thu">5</td><td class="fri">6</td><td class="sat">7</td><td class="sun">8</td></tr>
    <tr><td class="mon">9</td><td class="tue">10</td><td class="wed">11</td><td class="thu">12</td><td class="fri">13</td><td class="sat">14</td><td class="sun">15</td></tr>
    <tr><td class="mon">16</td><td class="tue">17</td><td class="wed">18</td><td class="thu">19</td><td class="fri">20</td><td class="sat">21</td><td class="sun">22</td></tr>
    <tr><td class="mon">23</td><td class="tue">24</td><td class="wed">25</td><td class="thu">26</td><td class="fri">27</td><td class="sat">28</td><td class="sun">29</td></tr>
    <tr><td class="mon">30</td><td class="tue">31</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td><td class="noday">&nbsp;</td></tr>
    </table>
    <BLANKLINE>
    """

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
