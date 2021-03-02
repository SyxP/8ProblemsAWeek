## -*- encoding: utf-8 -*-


# This file was *autogenerated* from the file HW4.sagetex.sage
from sage.all_cmdline import *   # import sage library

_sage_const_22 = Integer(22); _sage_const_27 = Integer(27); _sage_const_30 = Integer(30); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_31 = Integer(31); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_5 = Integer(5); _sage_const_32 = Integer(32); _sage_const_6 = Integer(6); _sage_const_33 = Integer(33); _sage_const_7 = Integer(7); _sage_const_34 = Integer(34); _sage_const_8 = Integer(8); _sage_const_37 = Integer(37); _sage_const_42 = Integer(42); _sage_const_45 = Integer(45); _sage_const_9 = Integer(9); _sage_const_10 = Integer(10); _sage_const_11 = Integer(11); _sage_const_46 = Integer(46); _sage_const_12 = Integer(12); _sage_const_13 = Integer(13); _sage_const_14 = Integer(14); _sage_const_47 = Integer(47); _sage_const_15 = Integer(15); _sage_const_48 = Integer(48); _sage_const_16 = Integer(16); _sage_const_49 = Integer(49); _sage_const_17 = Integer(17); _sage_const_52 = Integer(52); _sage_const_57 = Integer(57); _sage_const_60 = Integer(60); _sage_const_18 = Integer(18); _sage_const_19 = Integer(19); _sage_const_20 = Integer(20); _sage_const_61 = Integer(61); _sage_const_21 = Integer(21); _sage_const_23 = Integer(23); _sage_const_62 = Integer(62); _sage_const_24 = Integer(24); _sage_const_63 = Integer(63); _sage_const_25 = Integer(25); _sage_const_64 = Integer(64); _sage_const_26 = Integer(26); _sage_const_67 = Integer(67); _sage_const_72 = Integer(72); _sage_const_75 = Integer(75); _sage_const_28 = Integer(28); _sage_const_29 = Integer(29); _sage_const_76 = Integer(76); _sage_const_77 = Integer(77); _sage_const_78 = Integer(78); _sage_const_79 = Integer(79); _sage_const_35 = Integer(35)## This file (HW4.sagetex.sage) was *autogenerated* from HW4.tex with sagetex.sty version 2020/08/12 v3.5.
import sagetex
_st_ = sagetex.SageTeXProcessor('HW4', version='2020/08/12 v3.5', version_check=True)
_st_.current_tex_line = _sage_const_22 
_st_.blockbegin()
try:
         a,b,c,u,v = var('a,b,c,u,v')
         c1 = a*sin(u)*cos(v)
         c2 = b*sin(u)*sin(v)
         c3 = c*cos(u)
     
except:
 _st_.goboom(_sage_const_27 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_30 
 _st_.inline(_sage_const_0 , latex(diff(c1,u)))
except:
 _st_.goboom(_sage_const_30 )
try:
 _st_.current_tex_line = _sage_const_30 
 _st_.inline(_sage_const_1 , latex(diff(c2, u)))
except:
 _st_.goboom(_sage_const_30 )
try:
 _st_.current_tex_line = _sage_const_30 
 _st_.inline(_sage_const_2 , latex(diff(c3,u)))
except:
 _st_.goboom(_sage_const_30 )
try:
 _st_.current_tex_line = _sage_const_31 
 _st_.inline(_sage_const_3 , latex(diff(c1,v)))
except:
 _st_.goboom(_sage_const_31 )
try:
 _st_.current_tex_line = _sage_const_31 
 _st_.inline(_sage_const_4 , latex(diff(c2, v)))
except:
 _st_.goboom(_sage_const_31 )
try:
 _st_.current_tex_line = _sage_const_31 
 _st_.inline(_sage_const_5 , latex(diff(c3,v)))
except:
 _st_.goboom(_sage_const_31 )
try:
 _st_.current_tex_line = _sage_const_32 
 _st_.inline(_sage_const_6 , latex((diff(c1,u)**_sage_const_2  + diff(c2,u)**_sage_const_2  + diff(c3,u)**_sage_const_2 ).full_simplify()))
except:
 _st_.goboom(_sage_const_32 )
try:
 _st_.current_tex_line = _sage_const_33 
 _st_.inline(_sage_const_7 , latex((diff(c1,u)*diff(c1,v) + diff(c2,u)*diff(c2,v) + diff(c2,u)*diff(c2,v)).full_simplify()))
except:
 _st_.goboom(_sage_const_33 )
try:
 _st_.current_tex_line = _sage_const_34 
 _st_.inline(_sage_const_8 , latex((diff(c1,v)**_sage_const_2  + diff(c2,v)**_sage_const_2  + diff(c3,v)**_sage_const_2 ).full_simplify()))
except:
 _st_.goboom(_sage_const_34 )
_st_.current_tex_line = _sage_const_37 
_st_.blockbegin()
try:
         a,b,c,u,v = var('a,b,c,u,v')
         c1 = a*u*cos(v)
         c2 = b*u*sin(v)
         c3 = u**_sage_const_2 
     
except:
 _st_.goboom(_sage_const_42 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_45 
 _st_.inline(_sage_const_9 , latex(diff(c1,u)))
except:
 _st_.goboom(_sage_const_45 )
try:
 _st_.current_tex_line = _sage_const_45 
 _st_.inline(_sage_const_10 , latex(diff(c2, u)))
except:
 _st_.goboom(_sage_const_45 )
try:
 _st_.current_tex_line = _sage_const_45 
 _st_.inline(_sage_const_11 , latex(diff(c3,u)))
except:
 _st_.goboom(_sage_const_45 )
try:
 _st_.current_tex_line = _sage_const_46 
 _st_.inline(_sage_const_12 , latex(diff(c1,v)))
except:
 _st_.goboom(_sage_const_46 )
try:
 _st_.current_tex_line = _sage_const_46 
 _st_.inline(_sage_const_13 , latex(diff(c2, v)))
except:
 _st_.goboom(_sage_const_46 )
try:
 _st_.current_tex_line = _sage_const_46 
 _st_.inline(_sage_const_14 , latex(diff(c3,v)))
except:
 _st_.goboom(_sage_const_46 )
try:
 _st_.current_tex_line = _sage_const_47 
 _st_.inline(_sage_const_15 , latex((diff(c1,u)**_sage_const_2  + diff(c2,u)**_sage_const_2  + diff(c3,u)**_sage_const_2 ).full_simplify()))
except:
 _st_.goboom(_sage_const_47 )
try:
 _st_.current_tex_line = _sage_const_48 
 _st_.inline(_sage_const_16 , latex((diff(c1,u)*diff(c1,v) + diff(c2,u)*diff(c2,v) + diff(c2,u)*diff(c2,v)).full_simplify()))
except:
 _st_.goboom(_sage_const_48 )
try:
 _st_.current_tex_line = _sage_const_49 
 _st_.inline(_sage_const_17 , latex((diff(c1,v)**_sage_const_2  + diff(c2,v)**_sage_const_2  + diff(c3,v)**_sage_const_2 ).full_simplify()))
except:
 _st_.goboom(_sage_const_49 )
_st_.current_tex_line = _sage_const_52 
_st_.blockbegin()
try:
         a,b,c,u,v = var('a,b,c,u,v')
         c1 = a*u*cosh(v)
         c2 = b*u*sinh(v)
         c3 = u**_sage_const_2 
     
except:
 _st_.goboom(_sage_const_57 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_60 
 _st_.inline(_sage_const_18 , latex(diff(c1,u)))
except:
 _st_.goboom(_sage_const_60 )
try:
 _st_.current_tex_line = _sage_const_60 
 _st_.inline(_sage_const_19 , latex(diff(c2, u)))
except:
 _st_.goboom(_sage_const_60 )
try:
 _st_.current_tex_line = _sage_const_60 
 _st_.inline(_sage_const_20 , latex(diff(c3,u)))
except:
 _st_.goboom(_sage_const_60 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_21 , latex(diff(c1,v)))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_22 , latex(diff(c2, v)))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_61 
 _st_.inline(_sage_const_23 , latex(diff(c3,v)))
except:
 _st_.goboom(_sage_const_61 )
try:
 _st_.current_tex_line = _sage_const_62 
 _st_.inline(_sage_const_24 , latex((diff(c1,u)**_sage_const_2  + diff(c2,u)**_sage_const_2  + diff(c3,u)**_sage_const_2 ).full_simplify()))
except:
 _st_.goboom(_sage_const_62 )
try:
 _st_.current_tex_line = _sage_const_63 
 _st_.inline(_sage_const_25 , latex((diff(c1,u)*diff(c1,v) + diff(c2,u)*diff(c2,v) + diff(c2,u)*diff(c2,v)).full_simplify()))
except:
 _st_.goboom(_sage_const_63 )
try:
 _st_.current_tex_line = _sage_const_64 
 _st_.inline(_sage_const_26 , latex((diff(c1,v)**_sage_const_2  + diff(c2,v)**_sage_const_2  + diff(c3,v)**_sage_const_2 ).full_simplify()))
except:
 _st_.goboom(_sage_const_64 )
_st_.current_tex_line = _sage_const_67 
_st_.blockbegin()
try:
         a,b,c,u,v = var('a,b,c,u,v')
         c1 = a*sinh(u)*cos(v)
         c2 = b*sinh(u)*sin(v)
         c3 = c*cosh(u)
     
except:
 _st_.goboom(_sage_const_72 )
_st_.blockend()
try:
 _st_.current_tex_line = _sage_const_75 
 _st_.inline(_sage_const_27 , latex(diff(c1,u)))
except:
 _st_.goboom(_sage_const_75 )
try:
 _st_.current_tex_line = _sage_const_75 
 _st_.inline(_sage_const_28 , latex(diff(c2, u)))
except:
 _st_.goboom(_sage_const_75 )
try:
 _st_.current_tex_line = _sage_const_75 
 _st_.inline(_sage_const_29 , latex(diff(c3,u)))
except:
 _st_.goboom(_sage_const_75 )
try:
 _st_.current_tex_line = _sage_const_76 
 _st_.inline(_sage_const_30 , latex(diff(c1,v)))
except:
 _st_.goboom(_sage_const_76 )
try:
 _st_.current_tex_line = _sage_const_76 
 _st_.inline(_sage_const_31 , latex(diff(c2, v)))
except:
 _st_.goboom(_sage_const_76 )
try:
 _st_.current_tex_line = _sage_const_76 
 _st_.inline(_sage_const_32 , latex(diff(c3,v)))
except:
 _st_.goboom(_sage_const_76 )
try:
 _st_.current_tex_line = _sage_const_77 
 _st_.inline(_sage_const_33 , latex((diff(c1,u)**_sage_const_2  + diff(c2,u)**_sage_const_2  + diff(c3,u)**_sage_const_2 ).full_simplify()))
except:
 _st_.goboom(_sage_const_77 )
try:
 _st_.current_tex_line = _sage_const_78 
 _st_.inline(_sage_const_34 , latex((diff(c1,u)*diff(c1,v) + diff(c2,u)*diff(c2,v) + diff(c2,u)*diff(c2,v)).full_simplify()))
except:
 _st_.goboom(_sage_const_78 )
try:
 _st_.current_tex_line = _sage_const_79 
 _st_.inline(_sage_const_35 , latex((diff(c1,v)**_sage_const_2  + diff(c2,v)**_sage_const_2  + diff(c3,v)**_sage_const_2 ).full_simplify()))
except:
 _st_.goboom(_sage_const_79 )
_st_.endofdoc()

