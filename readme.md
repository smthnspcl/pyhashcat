## pyhashcat

Python C API binding to libhashcat, originally written by Rich5. <br>
Updated to use the latest Hashcat version, with additional functionality added. 

Pulled from [here](https://github.com/Rich5/pyhashcat/tree/master/pyhashcat)<br>
and ported to Python v3 [here](https://github.com/initiate6/pyhashcat/tree/master/pyhashcat)

pyhashcat has been completely rewritten as a Python C extension to interface directly with libhashcat. <br>
The pyhashcat module now acts as direct bindings to hashcat.

Requirements: 
* libhashcat
* Python 3

#### how to...
##### install:
```
./setup.sh
```

##### test:
```
$ python3 tests/simple_mask.py
-------------------------------
---- Simple pyhashcat Test ----
-------------------------------
[+] Running hashcat
... snip
STATUS:  Cracked
8743b52063cd84097a65d1633f5c74f5  -->  hashcat
```

#### help:

```
CLion / PyCharm will give good autocompletion, even for the Hashcat object

else: 

import pyhashcat
help(pyhashcat)

Help on module pyhashcat:

NAME
    pyhashcat - Python Bindings for hashcat

CLASSES
    builtins.Exception(builtins.BaseException)
        hashcat.error
    builtins.object
        hashcat
    
    Hashcat = class hashcat(builtins.object)
     |  Python bindings for hashcat
     |  
     |  Methods defined here:
     |  
     |  event_connect(...)
     |      event_connect(callback, signal)
     |      
     |      Register callback with dispatcher. Callback will trigger on signal specified
     |  
     |  hashcat_session_bypass(...)
     |      hashcat_session_bypass -> int
     |      
     |      Bypass current attack and go to next. Only applicable when using multiple wordlists or masks
     |      
     |      Return 0 on success, -1 on error
     |  
     |  hashcat_session_checkpoint(...)
     |      hashcat_session_checkpoint -> int
     |      
     |      Stop at next restore point. This feature is disabled when restore_disabled is specified, and will return error
     |      
     |      Return 0 on success, -1 on error
     |  
     |  hashcat_session_execute(...)
     |      hashcat_session_execute -> int
     |      
     |      Start hashcat cracking session in background thread.
     |      
     |      Return 0 on successful thread creation, pthread error number otherwise
     |  
     |  hashcat_session_pause(...)
     |      hashcat_session_pause -> int
     |      
     |      Pause hashcat cracking session.
     |      
     |      Return 0 on success, -1 on error
     |  
     |  hashcat_session_quit(...)
     |      hashcat_session_quit -> int
     |      
     |      Quit hashcat session.
     |      
     |      Return 0 on success otherwise -1
     |  
     |  hashcat_session_resume(...)
     |      hashcat_session_resume -> int
     |      
     |      Resume hashcat cracking session.
     |      
     |      Return 0 on success, -1 on error
     |  
     |  hashcat_status_get_status(...)
     |      Return status info struct as a Python dictionary
     |  
     |  reset(...)
     |      hashcat_reset
     |      
     |      Completely reset hashcat session to defaults.
     |  
     |  status_get_corespeed_dev(...)
     |      status_get_corespeed_dev(device_id) -> int
     |      
     |      Return device corespeed.
     |  
     |  status_get_cpt(...)
     |      status_get_cpt -> str
     |      
     |      Return string representation of cracked stats.
     |  
     |  status_get_cpt_avg_day(...)
     |      status_get_cpt_avg_day -> double
     |      
     |      Return averaged cracked per time (day).
     |  
     |  status_get_cpt_avg_hour(...)
     |      status_get_cpt_avg_hour -> double
     |      
     |      Return averaged cracked per time (hour).
     |  
     |  status_get_cpt_avg_min(...)
     |      status_get_cpt_avg_min -> double
     |      
     |      Return averaged cracked per time (min).
     |  
     |  status_get_cpt_cur_day(...)
     |      status_get_cpt_cur_day -> int
     |      
     |      Return cracked per time (day).
     |  
     |  status_get_cpt_cur_hour(...)
     |      status_get_cpt_cur_hour -> int
     |      
     |      Return cracked per time (hour).
     |  
     |  status_get_cpt_cur_min(...)
     |      status_get_cpt_cur_min -> int
     |      
     |      Return cracked per time (min).
     |  
     |  status_get_device_info_active(...)
     |      status_get_device_info_active -> int
     |      
     |      Return number of active devices.
     |  
     |  status_get_device_info_cnt(...)
     |      status_get_device_info_cnt -> int
     |      
     |      Return number of devices. (i.e. CPU, GPU, FPGA, DSP, Co-Processor)
     |  
     |  status_get_digests_cnt(...)
     |      status_get_digests_cnt -> int
     |      
     |      Return total number of digests (digests_cnt).
     |  
     |  status_get_digests_done(...)
     |      status_get_digests_done -> int
     |      
     |      Return number of completed digests (digests_done).
     |  
     |  status_get_digests_percent(...)
     |      status_get_digests_percent -> double
     |      
     |      Return percentage of completed digests (digests_done/digests_cnt).
     |  
     |  status_get_exec_msec_all(...)
     |      status_get_exec_msec_all -> int
     |      
     |      Return total execution time in msec for all devices.
     |  
     |  status_get_exec_msec_dev(...)
     |      status_get_exec_msec_dev(device_id) -> int
     |      
     |      Return execution time in msec for specific device.
     |  
     |  status_get_guess_base(...)
     |      status_get_guess_base -> str
     |      
     |      Return base input source.
     |      
     |      DETAILS:
     |      Depending on the mode the input base could be dict1, dict2, or mask.
     |  
     |  status_get_guess_base_count(...)
     |      status_get_guess_base_count -> int
     |      
     |      Return base input count.
     |  
     |  status_get_guess_base_offset(...)
     |      status_get_guess_base_offset -> int
     |      
     |      Return base input offset.
     |  
     |  status_get_guess_base_percent(...)
     |      status_get_guess_base_percent -> double
     |      
     |      Return base input percent.
     |  
     |  status_get_guess_candidates_dev(...)
     |      status_get_guess_candidates_dev(device_id) -> str
     |      
     |      Return candidate status string for a device.
     |  
     |  status_get_guess_charset(...)
     |      status_get_guess_charset -> str
     |      
     |      Return charset used during session.
     |  
     |  status_get_guess_mask_length(...)
     |      status_get_guess_mask_length -> int
     |      
     |      Return length of input mask.
     |  
     |  status_get_guess_mod(...)
     |      status_get_guess_mod -> str
     |      
     |      Return input modification.
     |      
     |      DETAILS:
     |      Depending on the mode the mod could be rules file, dict1, dict2, or mask.
     |  
     |  status_get_guess_mod_count(...)
     |      status_get_guess_mod_count -> int
     |      
     |      Return input modification count.
     |  
     |  status_get_guess_mod_offset(...)
     |      status_get_guess_mod_offset -> int
     |      
     |      Return input modification offset.
     |  
     |  status_get_guess_mod_percent(...)
     |      status_get_guess_mod_percent -> double
     |      
     |      Return input modification percent.
     |  
     |  status_get_guess_mode(...)
     |      status_get_guess_mode -> int
     |      
     |      Return input mode.
     |      
     |      DETAILS:
     |              GUESS_MODE_NONE                       = 0
     |              GUESS_MODE_STRAIGHT_FILE              = 1
     |              GUESS_MODE_STRAIGHT_FILE_RULES_FILE   = 2
     |              GUESS_MODE_STRAIGHT_FILE_RULES_GEN    = 3
     |              GUESS_MODE_STRAIGHT_STDIN             = 4
     |              GUESS_MODE_STRAIGHT_STDIN_RULES_FILE  = 5
     |              GUESS_MODE_STRAIGHT_STDIN_RULES_GEN   = 6
     |              GUESS_MODE_COMBINATOR_BASE_LEFT       = 7
     |              GUESS_MODE_COMBINATOR_BASE_RIGHT      = 8
     |              GUESS_MODE_MASK                       = 9
     |              GUESS_MODE_MASK_CS                    = 10
     |              GUESS_MODE_HYBRID1                    = 11
     |              GUESS_MODE_HYBRID1_CS                 = 12
     |              GUESS_MODE_HYBRID2                    = 13
     |              GUESS_MODE_HYBRID2_CS                 = 14
     |  
     |  status_get_hash_name(...)
     |      status_get_hash_name -> str
     |      
     |      Return type of hash.
     |  
     |  status_get_hash_target(...)
     |      status_get_hash_target -> str
     |      
     |      Return hash or hash file for current session.
     |  
     |  status_get_hashes_msec_all(...)
     |      status_get_hashes_msec_all -> int
     |      
     |      Return total time to attempt a hash in msec for all devices.
     |  
     |  status_get_hashes_msec_dev(...)
     |      status_get_hashes_msec_dev(device_id) -> int
     |      
     |      Return time to attempt a hash in msec for specific device.
     |  
     |  status_get_hashes_msec_dev_benchmark(...)
     |      status_get_hashes_msec_dev_benchmark(device_id) -> int
     |      
     |      Return time to attempt a hash in msec for specific device (bendmark mode).
     |  
     |  status_get_hwmon_dev(...)
     |      status_get_hwmon_dev(device_id) -> str
     |      
     |      Return device stats.
     |      
     |      DETAILS:
     |              Temp
     |              Fan
     |              Util
     |              Core (Mhz)
     |              Mem
     |              Lanes
     |              N/A
     |  
     |  status_get_memoryspeed_dev(...)
     |      status_get_memoryspeed_dev(device_id) -> int
     |      
     |      Return device memoryspeed.
     |  
     |  status_get_msec_paused(...)
     |      status_get_msec_paused -> double
     |      
     |      Return paused time in msec.
     |  
     |  status_get_msec_real(...)
     |      status_get_msec_real -> double
     |      
     |      Return running time plus paused time in msec.
     |  
     |  status_get_msec_running(...)
     |      status_get_msec_running -> double
     |      
     |      Return running time in msec.
     |  
     |  status_get_progress_cur(...)
     |      status_get_progress_cur -> int
     |      
     |      Return current restore progress.
     |  
     |  status_get_progress_cur_relative_skip(...)
     |      status_get_progress_cur_relative_skip -> int
     |      
     |      Return number of cracked hashes.
     |  
     |  status_get_progress_dev(...)
     |      status_get_progress_dev(device_id) -> int
     |      
     |      Return device progress (keyspace).
     |  
     |  status_get_progress_done(...)
     |      status_get_progress_done -> int
     |      
     |      Return number of password candidates attempted.
     |  
     |  status_get_progress_end(...)
     |      status_get_progress_end -> int
     |      
     |      Return high limit of restore progress.
     |  
     |  status_get_progress_end_relative_skip(...)
     |      status_get_progress_end_relative_skip -> int
     |      
     |      Return total hashes targeted for cracking during session.
     |  
     |  status_get_progress_finished_percent(...)
     |      status_get_progress_finished_percent -> double
     |      
     |      Return progress percentage (progress_cur_relative_skip/progress_end_relative_skip).
     |  
     |  status_get_progress_ignore(...)
     |      status_get_progress_ignore -> int
     |      
     |      Return ignore progress.
     |  
     |  status_get_progress_mode(...)
     |      status_get_progress_mode -> int
     |      
     |      Return progress mode.
     |      
     |      DETAILS:
     |              PROGRESS_MODE_NONE              = 0
     |              PROGRESS_MODE_KEYSPACE_KNOWN    = 1
     |              PROGRESS_MODE_KEYSPACE_UNKNOWN  = 2
     |  
     |  status_get_progress_rejected(...)
     |      status_get_progress_rejected -> int
     |      
     |      Return number of password candidates rejected.
     |  
     |  status_get_progress_rejected_percent(...)
     |      status_get_progress_rejected_percent -> double
     |      
     |      Return percentage rejected candidates (progress_rejected/progress_cur).
     |  
     |  status_get_progress_restored(...)
     |      status_get_progress_restored -> int
     |      
     |      Return restore progress completed.
     |  
     |  status_get_progress_skip(...)
     |      status_get_progress_skip -> int
     |      
     |      Return skip progress.
     |  
     |  status_get_restore_percent(...)
     |      status_get_restore_percent -> double
     |      
     |      Return percentage of keyspace covered (restore_point/restore_total).
     |  
     |  status_get_restore_point(...)
     |      status_get_restore_point -> int
     |      
     |      Return restore point current position.
     |  
     |  status_get_restore_total(...)
     |      status_get_restore_total -> int
     |      
     |      Return total key space.
     |  
     |  status_get_runtime_msec_dev(...)
     |      status_get_runtime_msec_dev(device_id) -> double
     |      
     |      Return device runtime (ms).
     |  
     |  status_get_salts_cnt(...)
     |      status_get_salts_cnt -> int
     |      
     |      Return total number of salts (salts_cnt).
     |  
     |  status_get_salts_done(...)
     |      status_get_salts_done -> int
     |      
     |      Return number of completed salts (salts_done).
     |  
     |  status_get_salts_percent(...)
     |      status_get_salts_percent -> double
     |      
     |      Return percentage of completed salts (salts_done/salts_cnt).
     |  
     |  status_get_session(...)
     |      status_get_session -> str
     |      
     |      Return session string set at run time.
     |  
     |  status_get_skipped_dev(...)
     |      status_get_skipped_dev(device_id) -> bool
     |      
     |      Return True if device status is skipped.
     |  
     |  status_get_speed_sec_all(...)
     |      status_get_speed_sec_all(device_id) -> str
     |      
     |      Return total combine speed of all devices.
     |  
     |  status_get_speed_sec_dev(...)
     |      status_get_speed_sec_dev(device_id) -> str
     |      
     |      Return speed of device.
     |  
     |  status_get_status_number(...)
     |      status_get_status_number -> int
     |      
     |      Return session number set at run time.
     |      
     |      DETAILS:
     |              Initializing->ST_0000
     |              Autotuning->ST_0001
     |              Running->ST_0002
     |              Paused->ST_0003
     |              Exhausted->ST_0004
     |              Cracked->ST_0005
     |              Aborted->ST_0006
     |              Quit->ST_0007
     |              Bypass->ST_0008
     |              Aborted (Checkpoint)->ST_0009
     |              Aborted (Runtime)->ST_0010
     |  
     |  status_get_status_string(...)
     |      status_get_skipped_dev -> str
     |      
     |      Return session string set at run time.
     |      
     |      DETAILS:
     |              Initializing
     |              Autotuning
     |              Running
     |              Paused
     |              Exhausted
     |              Cracked
     |              Aborted
     |              Quit
     |              Bypass
     |              Aborted (Checkpoint)
     |              Aborted (Runtime)
     |              Unknown! Bug!
     |  
     |  status_get_time_estimated_absolute(...)
     |      status_get_time_estimated_absolute -> str
     |      
     |      Return string representation of estimated time.
     |      DETAILS:
     |      Thu Jan 1 21:49:08 1970
     |  
     |  status_get_time_estimated_relative(...)
     |      status_get_time_estimated_relative -> str
     |      
     |      Return string representation of estimated time relative to now.
     |      
     |      DETAILS:
     |              5 secs
     |              5 mins
     |              5 hours
     |              5 days
     |              5 years
     |  
     |  status_get_time_started_absolute(...)
     |      status_get_time_started_absolute -> str
     |      
     |      Return string representation of start time.
     |      
     |      DETAILS:
     |      Thu Jan 1 21:49:08 1970
     |  
     |  status_get_time_started_relative(...)
     |      status_get_time_started_relative -> str
     |      
     |      Return string representation of elapsed time relative to start.
     |      
     |      DETAILS:
     |              5 secs
     |              5 mins
     |              5 hours
     |              5 days
     |              5 years
     |  
     |  ----------------------------------------------------------------------
     |  Static methods defined here:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors defined here:
     |  
     |  attack_mode
     |      attack_mode     int     See reference below
     |      
     |      Reference:
     |              0 | Straight
     |              1 | Combination
     |              3 | Brute-force
     |              6 | Hybrid Wordlist + Mask
     |              7 | Hybrid Mask + Wordlist
     |  
     |  benchmark
     |      benchmark       bool    Run benchmark
     |  
     |  bitmap_max
     |      bitmap_max      int     Sets maximum bits allowed for bitmaps to X
     |  
     |  bitmap_min
     |      bitmap_min      int     Sets minimum bits allowed for bitmaps to X
     |  
     |  brain_client
     |      brain_client -> bool
     |      
     |      Get/set brain client mode.
     |  
     |  brain_client_features
     |      brain_client_features-> int
     |      
     |      Get/set brain client features.
     |  
     |  brain_host
     |      brain_host -> str
     |      
     |      Get/set brain server host IP address.
     |  
     |  brain_password
     |      brain_password -> str
     |      
     |      Get/set brain password.
     |  
     |  brain_port
     |      brain_port -> int
     |      
     |      Get/set brain server TCP port number.
     |  
     |  brain_server
     |      brain_server -> bool
     |      
     |      Get/set brain server mode.
     |  
     |  brain_session
     |      brain_session-> int
     |      
     |      Get/set brain session.
     |  
     |  brain_session_whitelist
     |      brain_session_whitelist -> str
     |      
     |      Get/set brain session whitelist.
     |  
     |  cpu_affinity
     |      cpu_affinity    str     Locks to CPU devices, separate with comma
     |  
     |  custom_charset_1
     |      custom_charset_1        str      User-defined charset ?1
     |  
     |  custom_charset_2
     |      custom_charset_2        str      User-defined charset ?2
     |  
     |  custom_charset_3
     |      custom_charset_3        str      User-defined charset ?3
     |  
     |  custom_charset_4
     |      custom_charset_4        str      User-defined charset ?4
     |  
     |  debug_file
     |      debug_file      str     Output file for debugging rules
     |  
     |  debug_mode
     |      debug_mode      int     Defines the debug mode (hybrid only by using rules) 
     |      
     |      REFERENCE:
     |              1 | Finding-Rule
     |              2 | Original-Word
     |              3 | Original-Word:Finding-Rule
     |              4 | Original-Word:Finding-Rule:Processed-Word
     |  
     |  dict1
     |      dict1   str     dictionary|directory
     |  
     |  dict2
     |      dict2   str     dictionary
     |  
     |  event_types
     |      event_types     tuple   Reference list of event signals to use for callbacks
     |      
     |      DETAILS:
     |      Signals are used to bind callbacks to hashcat events.
     |      Ex: hc.event_connect(callback=cracked_callback, signal="EVENT_CRACKER_HASH_CRACKED")
     |  
     |  force
     |      force   bool    Ignore warnings
     |  
     |  hash
     |      hash    str     hash|hashfile|hccapfile
     |  
     |  hash_mode
     |      hash_mode       int     Hash-type, see references
     |  
     |  hex_charset
     |      hex_charset     bool    Assume charset is given in hex
     |  
     |  hex_salt
     |      hex_salt        bool    Assume salt is given in hex
     |  
     |  hex_wordlist
     |      hex_wordlist    bool    Assume words in wordlist is given in hex
     |  
     |  hwmon_disable
     |      hwmon_disable   bool    Disable temperature and fanspeed reads and triggers
     |  
     |  hwmon_temp_abort
     |      hwmon_temp_abort        int     Abort if GPU temperature reaches X degrees celsius
     |  
     |  increment
     |      increment       bool    Enable mask increment mode
     |  
     |  increment_max
     |      increment_max   int     Stop mask incrementing at X
     |  
     |  increment_min
     |      increment_min   int     Start mask incrementing at X
     |  
     |  induction_dir
     |      induction_dir   str     Specify the induction directory to use for loopback
     |  
     |  keep_guessing
     |      keep_guessing   bool    Keep guessing the hash after it has been cracked
     |  
     |  kernel_accel
     |      kernel_accel    int     Manual workload tuning, set outerloop step size to X
     |  
     |  kernel_loops
     |      kernel_loops    int     Manual workload tuning, set innerloop step size to X
     |  
     |  keyspace
     |      keyspace        bool    Show keyspace base:mod values and quit
     |  
     |  left
     |      left    str     Single rule applied to each word from left wordlist
     |  
     |  limit
     |      limit   int     Limit X words from the start + skipped words
     |  
     |  logfile_disable
     |      logfile_disable bool    Disable the logfile
     |  
     |  loopback
     |      loopback        bool    Add new plains to induct directory
     |  
     |  machine_readable
     |      machine_readable        bool    Display the status view in a machine readable format
     |  
     |  markov_classic
     |      markov_classic  bool    Enables classic markov-chains, no per-position
     |  
     |  markov_disable
     |      markov_disable  bool    Disables markov-chains, emulates classic brute-force
     |  
     |  markov_hcstat2
     |      markov_hcstat2  str     Specify hcstat file to use
     |  
     |  markov_threshold
     |      markov_threshold        int     Threshold X when to stop accepting new markov-chains
     |  
     |  mask
     |      mask    str     mask|directory
     |  
     |  opencl_device_types
     |      opencl_device_types     str     OpenCL device-types to use, separate with comma
     |      
     |      REFERENCE:
     |              1 | CPU
     |              2 | GPU
     |              3 | FPGA, DSP, Co-Processor
     |  
     |  opencl_devices
     |      opencl_devices  str     OpenCL devices to use, separate with comma
     |  
     |  opencl_info
     |      opencl_info     bool    Show info about OpenCL platforms/devices detected
     |  
     |  opencl_vector_width
     |      opencl_vector_width     int     Manual override OpenCL vector-width to X
     |  
     |  optimized_kernel_enable
     |      optimized_kernel_enable bool    Enable optimized kernel (-O)
     |  
     |  outfile
     |      outfile str     Define outfile for recovered hash
     |  
     |  outfile_autohex
     |      outfile_autohex bool    Disable the use of $HEX[] in output plains
     |  
     |  outfile_check_dir
     |      outfile_check_dir       str     Specify the outfile directory to monitor for plains
     |  
     |  outfile_check_timer
     |      outfile_check_timer     int     Sets seconds between outfile checks to X
     |  
     |  outfile_format
     |      outfile_format  int     Define outfile-format X for recovered hash
     |      
     |      REFERENCE:
     |              1  | hash[:salt]
     |              2  | plain
     |              3  | hash[:salt]:plain
     |              4  | hex_plain
     |              5  | hash[:salt]:hex_plain
     |              6  | plain:hex_plain
     |              7  | hash[:salt]:plain:hex_plain
     |              8  | crackpos
     |              9  | hash[:salt]:crack_pos
     |              10 | plain:crack_pos
     |              11 | hash[:salt]:plain:crack_pos
     |              12 | hex_plain:crack_pos
     |              13 | hash[:salt]:hex_plain:crack_pos
     |              14 | plain:hex_plain:crack_pos
     |              15 | hash[:salt]:plain:hex_plain:crack_pos
     |  
     |  potfile_disable
     |      potfile_disable bool    Do not write potfile
     |  
     |  potfile_path
     |      potfile_path    str     Specific path to potfile
     |  
     |  progress_only
     |      progress_only   bool    Quickly provides ideal progress step size and time to process on the user hashes and selected options, then quit
     |  
     |  quiet
     |      quiet   bool    Suppress output
     |  
     |  remove
     |      remove  bool    Enable remove of hash once it is cracked
     |  
     |  remove_timer
     |      remove_timer    int     Update input hash file each X seconds
     |  
     |  restore
     |      restore bool    Restore session from session = "session name"
     |  
     |  restore_disable
     |      restore_disable bool    Do not write restore file
     |  
     |  restore_file_path
     |      restore_file_path       bool    Specific path to restore file
     |  
     |  restore_timer
     |      restore_timer   int     TBD
     |  
     |  rp_files_cnt
     |      rp_files_cnt    int     rp_files_cnt, count of rp_files specified
     |  
     |  rp_gen
     |      rp_gen  int     Generate X random rules
     |  
     |  rp_gen_func_max
     |      rp_gen_func_max int     Force max X funcs per rule
     |  
     |  rp_gen_func_min
     |      rp_gen_func_min int     Force min X funcs per rule
     |  
     |  rp_gen_seed
     |      rp_gen_seed     int     Force RNG seed set to X
     |  
     |  rule_buf_l
     |      rule_buf_l      str     Single rule applied to each word from left wordlist
     |  
     |  rule_buf_r
     |      rule_buf_r      str     Single rule applied to each word from right wordlist
     |  
     |  rules
     |      rules   list    List of rules files to use
     |  
     |  runtime
     |      runtime int     Abort session after X seconds of runtime
     |  
     |  scrypt_tmto
     |      scrypt_tmto     int     Manually override TMTO value for scrypt to X
     |  
     |  segment_size
     |      segment_size    int     Sets size in MB to cache from the wordfile to X
     |  
     |  separator
     |      separator       char    Separator char for hashlists and outfile
     |  
     |  session
     |      session str     Define specific session name
     |  
     |  show
     |      show    bool    Compare hashlist with potfile; Show cracked hashes
     |  
     |  skip
     |      skip    int     Skip X words from the start
     |  
     |  speed_only
     |      speed_only      bool    Return expected speed of the attack and quit
     |  
     |  spin_damp
     |      spin_damp       int     Workaround NVidias CPU burning loop bug, in percent
     |  
     |  truecrypt_keyfiles
     |      truecrypt_keyfiles      str     Keyfiles used, separate with comma
     |  
     |  username
     |      username        bool    Enable ignoring of usernames in hashfile
     |  
     |  veracrypt_keyfiles
     |      veracrypt_keyfiles      str     Keyfiles used, separate with comma
     |  
     |  veracrypt_pim_start
     |      veracrypt_pim   int     VeraCrypt personal iterations multiplier start
     |  
     |  veracrypt_pim_stop
     |      veracrypt_pim   int     VeraCrypt personal iterations multiplier stop
     |  
     |  workload_profile
     |      workload_profile        int     Enable a specific workload profile, see pool below
     |      
     |      REFERENCE:
     |                          | Performance | Runtime | Power Consumption | Desktop Impact
     |              ------------+-------------+---------+-------------------+---------------
     |              1           | Low         |   2 ms  | Low               | Minimal
     |              2           | Default     |  12 ms  | Economic          | Noticeable
     |              3           | High        |  96 ms  | High              | Unresponsive
     |              4           | Nightmare   | 480 ms  | Insane            | Headless
    
    class error(builtins.Exception)
     |  Common base class for all non-exit exceptions.
     |  
     |  Method resolution order:
     |      error
     |      builtins.Exception
     |      builtins.BaseException
     |      builtins.object
     |  
     |  Data descriptors defined here:
     |  
     |  __weakref__
     |      list of weak references to the object (if defined)
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.Exception:
     |  
     |  __init__(self, /, *args, **kwargs)
     |      Initialize self.  See help(type(self)) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Static methods inherited from builtins.Exception:
     |  
     |  __new__(*args, **kwargs) from builtins.type
     |      Create and return a new object.  See help(type) for accurate signature.
     |  
     |  ----------------------------------------------------------------------
     |  Methods inherited from builtins.BaseException:
     |  
     |  __delattr__(self, name, /)
     |      Implement delattr(self, name).
     |  
     |  __getattribute__(self, name, /)
     |      Return getattr(self, name).
     |  
     |  __reduce__(...)
     |      Helper for pickle.
     |  
     |  __repr__(self, /)
     |      Return repr(self).
     |  
     |  __setattr__(self, name, value, /)
     |      Implement setattr(self, name, value).
     |  
     |  __setstate__(...)
     |  
     |  __str__(self, /)
     |      Return str(self).
     |  
     |  with_traceback(...)
     |      Exception.with_traceback(tb) --
     |      set self.__traceback__ to tb and return self.
     |  
     |  ----------------------------------------------------------------------
     |  Data descriptors inherited from builtins.BaseException:
     |  
     |  __cause__
     |      exception cause
     |  
     |  __context__
     |      exception context
     |  
     |  __dict__
     |  
     |  __suppress_context__
     |  
     |  __traceback__
     |  
     |  args
```
