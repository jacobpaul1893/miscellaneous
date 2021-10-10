#!/bin/bash
# print all users who have logged in in the last 24 hours
# time is computed from the time that the script is executed.
 
# ouput records are complete records from last. 
last -F -R | awk -v now="$( date "+%Y %m %d %H %M %S" )" '

     BEGIN {
        soup = "JanFebMarAprMayJunJulAugSepOctNovDec";
        dim = "030101001010";
        split( now, a, " " );           # compute timestamp for yesterday
        if( (a[3] = a[3] - 1) <= 0 )    # roll to prev month?
        {
            if( (a[2] = a[2] - 1) <= 0 )    # roll to prev year?
            {
                a[1]--;
                a[2] = 12;
                a[3] = 31;
            }
            else
            {
                a[3] = 31 - substr( dim, a[2], 1 );
                if( a[2] == 2 )
                    a[3] += a[1] % 4 == 0  ? ( a[1] % 100 != 0 ? 1 : (a[1]/400 == 0 ? 1 : 0)) : 0;  # adjust for leap year
            }
        }
        old_date = sprintf( "%4d%02d%02d%02d%02d%02d", a[1], a[2], a[3], a[4], a[5], a[6] ) +0;   # finally, yesterday at this time
    }

      NF < 6 || /reboot/ || /begins/ || /still logged/ { next; }   # ignore undesired records

    {
        gsub( ":", "", $6 );                                # build timestamp from last fields
        m = int(index( soup, $4 ) / 3) + 1;
        d = sprintf( "%4d%02d%02d%s", $7, m, $5, $6 ) + 0;
        if( d > old_date )                                  # if time newer than yesterday, print
            print;
    }'