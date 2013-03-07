# $Id: 323_srtp2_unsupported_crypto.py 2036 2008-06-20 17:43:55Z nanang $
import inc_sip as sip
import inc_sdp as sdp

sdp = \
"""
v=0
o=- 0 0 IN IP4 127.0.0.1
s=tester
c=IN IP4 127.0.0.1
t=0 0
m=audio 4000 RTP/SAVP 0 101
a=rtpmap:0 PCMU/8000
a=sendrecv
a=rtpmap:101 telephone-event/8000
a=fmtp:101 0-15
a=crypto:1 CRYPTO_X inline:WnD7c1ksDGs+dIefCEo8omPg4uO8DYIinNGL5yxQ
"""

args = "--null-audio --auto-answer 200 --max-calls 1 --use-srtp 2 --srtp-secure 0"
include = []
exclude = []

sendto_cfg = sip.SendtoCfg( "caller has used unsupported crypto, callee (SRTP mandatory) must reject the call", 
			    pjsua_args=args, sdp=sdp, resp_code=406, 
			    resp_inc=include, resp_exc=exclude)
