# Charming the Python on Nexus 7k Platform

I'm going to shorthand this tutorial's name to CTP so it's less cumbersome to name files.

## Show Commands

show hostname
show cdp neighbor
show cdp neighbor | xml
show ip int brief
show ip route local
show ip route ospf
show bgp ipv4 unicast summary
show ip route bgp
IPv6 will be configured in scenario 5
show ipv6 int brief
show bgp ipv6 unicast summary
show ipv6 route

___

## Help

*  If you want to ask for help on a particular object directly from the interpreter, you can enter: ‘help(“object”)
*  Omitting the double-quotes will fail. Importing the module is required to not use double-quotes.
    + to omit quotes you can enter the following
        - help()
        - pprint

### List of Modules

```python
CiscoLive_N7K# help> modules

Please wait a moment while I gather a list of all available modules...

Permission denied. ANSI                bsddb               importlib           screen
BaseHTTPServer      build_cmd_script    imputil             select
Bastion             build_cmd_script_from_file inspect             sets
CGIHTTPServer       bz2                 io                  sgmllib
ConfigParser        cPickle             itertools           sha
Cookie              cProfile            json                shelve
DocXMLRPCServer     cStringIO           keyword             shlex
FSM                 calendar            lib2to3             shutil
HTMLParser          cgi                 linecache           signal
MimeWriter          cgitb               linuxaudiodev       site
Queue               check_sys_st_op_consist locale              smtpd
SimpleHTTPServer    chunk               logging             smtplib
SimpleXMLRPCServer  cmath               macpath             snap_util
SocketServer        cmd                 macurl2path         snapshot_compare
StringIO            cmn_file_util       mailbox             sndhdr
UserDict            code                mailcap             socket
UserList            codecs              maintenance-mode    spwd
UserString          codeop              markupbase          sqlite3
_LWPCookieJar       collections         marshal             sre
_MozillaCookieJar   colorsys            math                sre_compile
__builtin__         commands            md5                 sre_constants
__future__          compileall          mhlib               sre_parse
_abcoll             compiler            mimetools           ssl
_ast                contextlib          mimetypes           stat
_bisect             convertipv4         mimify              statvfs
_bsddb              cookielib           mmap                string
_codecs             copy                modulefinder        stringold
_codecs_cn          copy_reg            msilib              stringprep
_codecs_hk          crypt               multifile           strop
_codecs_iso2022     csv                 multiprocessing     struct
_codecs_jp          ctypes              mutex               subprocess
_codecs_kr          curses              netrc               sunau
_codecs_tw          datetime            new                 sunaudio
_collections        dbhash              nis                 symbol
_csv                dbm                 nntplib             symtable
_ctypes             decimal             ntpath              syntaxtodoc
_ctypes_test        difflib             nturl2path          sys
_curses             dircache            numbers             sysconfig
_curses_panel       dis                 opcode              syslog
_elementtree        distutils           operator            tabnanny
_functools          dl                  optparse            tarfile
_hashlib            doctest             os                  telnetlib
_heapq              dumbdbm             os2emxpath          tempfile
_hotshot            dummy_thread        ossaudiodev         termios
_io                 dummy_threading     parser              textwrap
_json               email               pdb                 this
_locale             encodings           pexpect             thread
_lsprof             errno               pickle              threading
_multibytecodec     exceptions          pickletools         time
_multiprocessing    fcntl               pipejson            timeit
_pyio               fdpexpect           pipes               toaiff
_random             filecmp             pkgutil             token
_sha256             fileinput           platform            tokenize
_sha512             fnmatch             plistlib            trace
_socket             formatter           poap                traceback
_sre                fpformat            popen2              tty
_ssl                fractions           poplib              types
_strptime           ftplib              posix               unicodedata
_struct             functools           posixfile           unittest
_symtable           future_builtins     posixpath           update_cmd_script
_testcapi           gc                  pprint              urllib
_threading_local    gdbm                profile             urllib2
_tkinter            gen_sys_st_op       pstats              urlparse
_warnings           genericpath         pty                 user
_weakref            getopt              pwd                 uu
_weakrefset         getpass             pxssh               uuid
abc                 gettext             py_compile          warnings
aifc                glob                pyclbr              wave
antigravity         grp                 pydoc               weakref
anydbm              gzip                pydoc_data          webbrowser
argparse            hashlib             pyexpat             whichdb
array               heapq               quopri              wsgiref
ast                 hmac                random              xdrlib
asynchat            hotshot             re                  xml
asyncore            htmlentitydefs      readline            xmllib
atexit              htmllib             repr                xmlrpclib
audiodev            httplib             resource            xmltodict
audioop             idlelib             rexec               xxsubtype
base64              ihooks              rfc822              zipfile
bdb                 imageop             rlcompleter         zipimport
binascii            imaplib             robotparser         zlib
binhex              imghdr              runpy               
bisect              imp                 sched               

Enter any module name to get more help.  Or, type "modules spam" to search
for modules whose descriptions contain the word "spam".
```

### Help - 'Cisco' Module

```python
CiscoLive_N7K# help> cisco
system((less) 2>/dev/null): rejected!
Permission denied. Permission denied. Permission denied. Permission denied. Permission denied. Permission denied. system(more "/bootflash/tmpRpM0vK"): rejected!
Help on module cisco:

NAME
    cisco - commands that integrate with CLI

FILE
    (built-in)

CLASSES
    exceptions.Exception(exceptions.BaseException)
        cli_execution_error
        cli_syntax_error
    
    class cli_execution_error(exceptions.Exception)
     |  Method resolution order:
     |      cli_execution_error
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
-- more --
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
-- more --
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __reduce__(...)
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __setstate__(...)
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  __unicode__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |  
-- more --
     |  __dict__
     |  
     |  args
     |  
     |  message
    
    class cli_syntax_error(exceptions.Exception)
     |  Method resolution order:
     |      cli_syntax_error
     |      exceptions.Exception
     |      exceptions.BaseException
     |      __builtin__.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.Exception:
     |  
     |  __init__(...)
     |      x.__init__(...) initializes x; see help(type(x)) for signature
     |  
-- more --
     |  ----------------------------------------------------------------------
     |  Data and other attributes inherited from exceptions.Exception:
     |  
     |  __new__ = <built-in method __new__ of type object>
     |      T.__new__(S, ...) -> a new object with type S, a subtype of T
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from exceptions.BaseException:
     |  
     |  __delattr__(...)
     |      x.__delattr__('name') <==> del x.name
     |  
     |  __getattribute__(...)
     |      x.__getattribute__('name') <==> x.name
     |  
     |  __getitem__(...)
     |      x.__getitem__(y) <==> x[y]
     |  
     |  __getslice__(...)
     |      x.__getslice__(i, j) <==> x[i:j]
     |      
     |      Use of negative indices is not supported.
     |  
     |  __reduce__(...)
-- more --
     |  
     |  __repr__(...)
     |      x.__repr__() <==> repr(x)
     |  
     |  __setattr__(...)
     |      x.__setattr__('name', value) <==> x.name = value
     |  
     |  __setstate__(...)
     |  
     |  __str__(...)
     |      x.__str__() <==> str(x)
     |  
     |  __unicode__(...)
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from exceptions.BaseException:
     |  
     |  __dict__
     |  
     |  args
     |  
     |  message

FUNCTIONS
-- more --
    cli(...)
        execute a cli command
    
    clid(...)
        execute a cli command, return name/value pairs
    
    clip(...)
        execute a cli command, dont return it, just display it
    
    set_vrf(...)
        specify the vrf name for socket operations



CiscoLive_N7K# help>             
```

Referring to the above bullet, notice how removing the quotation marks compiles an error.

```python
CiscoLive_N7K# >>>  help(pprint)
  File "<stdin>", line 1
    help(pprint)
    ^
IndentationError: unexpected indent

CiscoLive_N7K# >>> help("pprint")
Help on module pprint:

NAME
    pprint - Support to pretty-print lists, tuples, & dictionaries recursively.

FILE
    /isan/python/scripts/pprint.py

DESCRIPTION
    Very simple, but useful, especially in debugging data structures.
    
    Classes
    -------
    
    PrettyPrinter()
        Handle pretty-printing operations onto a stream using a configured
        set of formatting parameters.
    
    Functions
    ---------
    
    pformat()
        Format a Python object into a pretty-printed representation.
    
-- more --
    pprint()
        Pretty-print a Python object to a stream [default is sys.stdout].
    
    saferepr()
        Generate a 'standard' repr()-like value, but protect against recursive
        data structures.

CLASSES
    PrettyPrinter
    
    class PrettyPrinter
     |  Methods defined here:
     |  
     |  __init__(self, indent=1, width=80, depth=None, stream=None)
     |      Handle pretty printing operations onto a stream using a set of
     |      configured parameters.
     |      
     |      indent
     |          Number of spaces to indent for each level of nesting.
     |      
     |      width
     |          Attempted maximum number of columns in the output.
     |      
     |      depth
-- more --
     |          The maximum depth to print out nested structures.
     |      
     |      stream
     |          The desired output stream.  If omitted (or false), the standard
     |          output stream available at construction will be used.
     |  
     |  format(self, object, context, maxlevels, level)
     |      Format object for a specific context, returning a string
     |      and flags indicating whether the representation is 'readable'
     |      and whether the object represents a recursive construct.
     |  
     |  isreadable(self, object)
     |  
     |  isrecursive(self, object)
     |  
     |  pformat(self, object)
     |  
     |  pprint(self, object)

FUNCTIONS
    isreadable(object)
        Determine if saferepr(object) is readable by eval().
    
    isrecursive(object)
-- more --
        Determine if object requires a recursive representation.
    
    pformat(object, indent=1, width=80, depth=None)
        Format a Python object into a pretty-printed representation.
    
    pprint(object, stream=None, indent=1, width=80, depth=None)
        Pretty-print a Python object to a stream [default is sys.stdout].
    
    saferepr(object)
        Version of repr() which can handle recursive data structures.

DATA
    __all__ = ['pprint', 'pformat', 'isreadable', 'isrecursive', 'saferepr...

```