#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 19:27:46 2022

@author: amirjonmurodov
"""

��U S E   [ m a s t e r ] 
 
 G O 
 
 / * * * * * *   O b j e c t :     D a t a b a s e   [ D B F I N A L ]         S c r i p t   D a t e :   2 4 . 0 6 . 2 0 2 2   1 5 : 4 0 : 0 6   * * * * * * / 
 
 C R E A T E   D A T A B A S E   [ D B F I N A L ] 
 
   C O N T A I N M E N T   =   N O N E 
 
   O N     P R I M A R Y   
 
 (   N A M E   =   N ' D B F I N A L ' ,   F I L E N A M E   =   N ' C : \ U s e r s \ b c e l e b i \ D B F I N A L . m d f '   ,   S I Z E   =   8 1 9 2 K B   ,   M A X S I Z E   =   U N L I M I T E D ,   F I L E G R O W T H   =   6 5 5 3 6 K B   ) 
 
   L O G   O N   
 
 (   N A M E   =   N ' D B F I N A L _ l o g ' ,   F I L E N A M E   =   N ' C : \ U s e r s \ b c e l e b i \ D B F I N A L _ l o g . l d f '   ,   S I Z E   =   8 1 9 2 K B   ,   M A X S I Z E   =   2 0 4 8 G B   ,   F I L E G R O W T H   =   6 5 5 3 6 K B   ) 
 
   W I T H   C A T A L O G _ C O L L A T I O N   =   D A T A B A S E _ D E F A U L T 
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   C O M P A T I B I L I T Y _ L E V E L   =   1 5 0 
 
 G O 
 
 I F   ( 1   =   F U L L T E X T S E R V I C E P R O P E R T Y ( ' I s F u l l T e x t I n s t a l l e d ' ) ) 
 
 b e g i n 
 
 E X E C   [ D B F I N A L ] . [ d b o ] . [ s p _ f u l l t e x t _ d a t a b a s e ]   @ a c t i o n   =   ' e n a b l e ' 
 
 e n d 
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A N S I _ N U L L _ D E F A U L T   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A N S I _ N U L L S   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A N S I _ P A D D I N G   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A N S I _ W A R N I N G S   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A R I T H A B O R T   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A U T O _ C L O S E   O N   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A U T O _ S H R I N K   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A U T O _ U P D A T E _ S T A T I S T I C S   O N   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   C U R S O R _ C L O S E _ O N _ C O M M I T   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   C U R S O R _ D E F A U L T     G L O B A L   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   C O N C A T _ N U L L _ Y I E L D S _ N U L L   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   N U M E R I C _ R O U N D A B O R T   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   Q U O T E D _ I D E N T I F I E R   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   R E C U R S I V E _ T R I G G E R S   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T     E N A B L E _ B R O K E R   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A U T O _ U P D A T E _ S T A T I S T I C S _ A S Y N C   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   D A T E _ C O R R E L A T I O N _ O P T I M I Z A T I O N   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   T R U S T W O R T H Y   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A L L O W _ S N A P S H O T _ I S O L A T I O N   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   P A R A M E T E R I Z A T I O N   S I M P L E   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   R E A D _ C O M M I T T E D _ S N A P S H O T   O N   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   H O N O R _ B R O K E R _ P R I O R I T Y   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   R E C O V E R Y   S I M P L E   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T     M U L T I _ U S E R   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   P A G E _ V E R I F Y   C H E C K S U M     
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   D B _ C H A I N I N G   O F F   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   F I L E S T R E A M (   N O N _ T R A N S A C T E D _ A C C E S S   =   O F F   )   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   T A R G E T _ R E C O V E R Y _ T I M E   =   6 0   S E C O N D S   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   D E L A Y E D _ D U R A B I L I T Y   =   D I S A B L E D   
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   A C C E L E R A T E D _ D A T A B A S E _ R E C O V E R Y   =   O F F     
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T   Q U E R Y _ S T O R E   =   O F F 
 
 G O 
 
 U S E   [ D B F I N A L ] 
 
 G O 
 
 / * * * * * *   O b j e c t :     U s e r   [ N e s n e T a b a n l 1O r n 2 ]         S c r i p t   D a t e :   2 4 . 0 6 . 2 0 2 2   1 5 : 4 0 : 0 6   * * * * * * / 
 
 C R E A T E   U S E R   [ N e s n e T a b a n l 1O r n 2 ]   F O R   L O G I N   [ N e s n e T a b a n l 1O r n 2 ]   W I T H   D E F A U L T _ S C H E M A = [ d b o ] 
 
 G O 
 
 / * * * * * *   O b j e c t :     T a b l e   [ d b o ] . [ _ _ E F M i g r a t i o n s H i s t o r y ]         S c r i p t   D a t e :   2 4 . 0 6 . 2 0 2 2   1 5 : 4 0 : 0 6   * * * * * * / 
 
 S E T   A N S I _ N U L L S   O N 
 
 G O 
 
 S E T   Q U O T E D _ I D E N T I F I E R   O N 
 
 G O 
 
 C R E A T E   T A B L E   [ d b o ] . [ _ _ E F M i g r a t i o n s H i s t o r y ] ( 
 
 	 [ M i g r a t i o n I d ]   [ n v a r c h a r ] ( 1 5 0 )   N O T   N U L L , 
 
 	 [ P r o d u c t V e r s i o n ]   [ n v a r c h a r ] ( 3 2 )   N O T   N U L L , 
 
   C O N S T R A I N T   [ P K _ _ _ E F M i g r a t i o n s H i s t o r y ]   P R I M A R Y   K E Y   C L U S T E R E D   
 
 ( 
 
 	 [ M i g r a t i o n I d ]   A S C 
 
 ) W I T H   ( P A D _ I N D E X   =   O F F ,   S T A T I S T I C S _ N O R E C O M P U T E   =   O F F ,   I G N O R E _ D U P _ K E Y   =   O F F ,   A L L O W _ R O W _ L O C K S   =   O N ,   A L L O W _ P A G E _ L O C K S   =   O N ,   O P T I M I Z E _ F O R _ S E Q U E N T I A L _ K E Y   =   O F F )   O N   [ P R I M A R Y ] 
 
 )   O N   [ P R I M A R Y ] 
 
 G O 
 
 / * * * * * *   O b j e c t :     T a b l e   [ d b o ] . [ A n a s a y f a ]         S c r i p t   D a t e :   2 4 . 0 6 . 2 0 2 2   1 5 : 4 0 : 0 6   * * * * * * / 
 
 S E T   A N S I _ N U L L S   O N 
 
 G O 
 
 S E T   Q U O T E D _ I D E N T I F I E R   O N 
 
 G O 
 
 C R E A T E   T A B L E   [ d b o ] . [ A n a s a y f a ] ( 
 
 	 [ I d ]   [ i n t ]   I D E N T I T Y ( 1 , 1 )   N O T   N U L L , 
 
 	 [ T e x t H e a d e r ]   [ n v a r c h a r ] ( 1 0 0 )   N U L L , 
 
 	 [ T e x t ]   [ n v a r c h a r ] ( 1 0 0 0 )   N U L L , 
 
 	 [ I m a g e ]   [ n v a r c h a r ] ( 5 0 )   N U L L , 
 
   C O N S T R A I N T   [ P K _ A n a s a y f a ]   P R I M A R Y   K E Y   C L U S T E R E D   
 
 ( 
 
 	 [ I d ]   A S C 
 
 ) W I T H   ( P A D _ I N D E X   =   O F F ,   S T A T I S T I C S _ N O R E C O M P U T E   =   O F F ,   I G N O R E _ D U P _ K E Y   =   O F F ,   A L L O W _ R O W _ L O C K S   =   O N ,   A L L O W _ P A G E _ L O C K S   =   O N ,   O P T I M I Z E _ F O R _ S E Q U E N T I A L _ K E Y   =   O F F )   O N   [ P R I M A R Y ] 
 
 )   O N   [ P R I M A R Y ] 
 
 G O 
 
 / * * * * * *   O b j e c t :     T a b l e   [ d b o ] . [ G a l e r i m ]         S c r i p t   D a t e :   2 4 . 0 6 . 2 0 2 2   1 5 : 4 0 : 0 6   * * * * * * / 
 
 S E T   A N S I _ N U L L S   O N 
 
 G O 
 
 S E T   Q U O T E D _ I D E N T I F I E R   O N 
 
 G O 
 
 C R E A T E   T A B L E   [ d b o ] . [ G a l e r i m ] ( 
 
 	 [ I d ]   [ i n t ]   I D E N T I T Y ( 1 , 1 )   N O T   N U L L , 
 
 	 [ P h o t o ]   [ n v a r c h a r ] ( 5 0 0 )   N U L L , 
 
 	 [ V i d e o ]   [ n v a r c h a r ] ( 5 0 0 )   N U L L , 
 
   C O N S T R A I N T   [ P K _ G a l e r i m ]   P R I M A R Y   K E Y   C L U S T E R E D   
 
 ( 
 
 	 [ I d ]   A S C 
 
 ) W I T H   ( P A D _ I N D E X   =   O F F ,   S T A T I S T I C S _ N O R E C O M P U T E   =   O F F ,   I G N O R E _ D U P _ K E Y   =   O F F ,   A L L O W _ R O W _ L O C K S   =   O N ,   A L L O W _ P A G E _ L O C K S   =   O N ,   O P T I M I Z E _ F O R _ S E Q U E N T I A L _ K E Y   =   O F F )   O N   [ P R I M A R Y ] 
 
 )   O N   [ P R I M A R Y ] 
 
 G O 
 
 / * * * * * *   O b j e c t :     T a b l e   [ d b o ] . [ H a k k i m d a ]         S c r i p t   D a t e :   2 4 . 0 6 . 2 0 2 2   1 5 : 4 0 : 0 6   * * * * * * / 
 
 S E T   A N S I _ N U L L S   O N 
 
 G O 
 
 S E T   Q U O T E D _ I D E N T I F I E R   O N 
 
 G O 
 
 C R E A T E   T A B L E   [ d b o ] . [ H a k k i m d a ] ( 
 
 	 [ I d ]   [ i n t ]   I D E N T I T Y ( 1 , 1 )   N O T   N U L L , 
 
 	 [ T e x t ]   [ n v a r c h a r ] ( 1 0 0 0 )   N U L L , 
 
 	 [ L i n k s ]   [ n v a r c h a r ] ( 5 0 0 )   N U L L , 
 
   C O N S T R A I N T   [ P K _ H a k k i m d a ]   P R I M A R Y   K E Y   C L U S T E R E D   
 
 ( 
 
 	 [ I d ]   A S C 
 
 ) W I T H   ( P A D _ I N D E X   =   O F F ,   S T A T I S T I C S _ N O R E C O M P U T E   =   O F F ,   I G N O R E _ D U P _ K E Y   =   O F F ,   A L L O W _ R O W _ L O C K S   =   O N ,   A L L O W _ P A G E _ L O C K S   =   O N ,   O P T I M I Z E _ F O R _ S E Q U E N T I A L _ K E Y   =   O F F )   O N   [ P R I M A R Y ] 
 
 )   O N   [ P R I M A R Y ] 
 
 G O 
 
 / * * * * * *   O b j e c t :     T a b l e   [ d b o ] . [ P r o j e l e r i m ]         S c r i p t   D a t e :   2 4 . 0 6 . 2 0 2 2   1 5 : 4 0 : 0 6   * * * * * * / 
 
 S E T   A N S I _ N U L L S   O N 
 
 G O 
 
 S E T   Q U O T E D _ I D E N T I F I E R   O N 
 
 G O 
 
 C R E A T E   T A B L E   [ d b o ] . [ P r o j e l e r i m ] ( 
 
 	 [ I d ]   [ i n t ]   I D E N T I T Y ( 1 , 1 )   N O T   N U L L , 
 
 	 [ P r o j e c t N a m e ]   [ n v a r c h a r ] ( 1 0 0 )   N U L L , 
 
 	 [ P r o j e c t D e s c r i p t i o n ]   [ n v a r c h a r ] ( 5 0 0 )   N U L L , 
 
 	 [ P r o j e c t Y e a r ]   [ n v a r c h a r ] ( 2 0 0 )   N U L L , 
 
   C O N S T R A I N T   [ P K _ P r o j e l e r i m ]   P R I M A R Y   K E Y   C L U S T E R E D   
 
 ( 
 
 	 [ I d ]   A S C 
 
 ) W I T H   ( P A D _ I N D E X   =   O F F ,   S T A T I S T I C S _ N O R E C O M P U T E   =   O F F ,   I G N O R E _ D U P _ K E Y   =   O F F ,   A L L O W _ R O W _ L O C K S   =   O N ,   A L L O W _ P A G E _ L O C K S   =   O N ,   O P T I M I Z E _ F O R _ S E Q U E N T I A L _ K E Y   =   O F F )   O N   [ P R I M A R Y ] 
 
 )   O N   [ P R I M A R Y ] 
 
 G O 
 
 / * * * * * *   O b j e c t :     T a b l e   [ d b o ] . [ U l a s i m ]         S c r i p t   D a t e :   2 4 . 0 6 . 2 0 2 2   1 5 : 4 0 : 0 6   * * * * * * / 
 
 S E T   A N S I _ N U L L S   O N 
 
 G O 
 
 S E T   Q U O T E D _ I D E N T I F I E R   O N 
 
 G O 
 
 C R E A T E   T A B L E   [ d b o ] . [ U l a s i m ] ( 
 
 	 [ I d ]   [ i n t ]   I D E N T I T Y ( 1 , 1 )   N O T   N U L L , 
 
 	 [ N a m e ]   [ n v a r c h a r ] ( 2 0 0 )   N U L L , 
 
 	 [ S u r n a m e ]   [ n v a r c h a r ] ( 2 0 0 )   N U L L , 
 
 	 [ E M a i l ]   [ n v a r c h a r ] ( 5 0 )   N U L L , 
 
 	 [ P h o n e N u m b e r ]   [ n v a r c h a r ] ( 2 0 )   N U L L , 
 
 	 [ M e s s a g e ]   [ n v a r c h a r ] ( 1 0 0 0 )   N U L L , 
 
   C O N S T R A I N T   [ P K _ U l a s i m ]   P R I M A R Y   K E Y   C L U S T E R E D   
 
 ( 
 
 	 [ I d ]   A S C 
 
 ) W I T H   ( P A D _ I N D E X   =   O F F ,   S T A T I S T I C S _ N O R E C O M P U T E   =   O F F ,   I G N O R E _ D U P _ K E Y   =   O F F ,   A L L O W _ R O W _ L O C K S   =   O N ,   A L L O W _ P A G E _ L O C K S   =   O N ,   O P T I M I Z E _ F O R _ S E Q U E N T I A L _ K E Y   =   O F F )   O N   [ P R I M A R Y ] 
 
 )   O N   [ P R I M A R Y ] 
 
 G O 
 
 I N S E R T   [ d b o ] . [ _ _ E F M i g r a t i o n s H i s t o r y ]   ( [ M i g r a t i o n I d ] ,   [ P r o d u c t V e r s i o n ] )   V A L U E S   ( N ' 2 0 2 2 0 5 2 5 1 3 3 5 2 8 _ W e b P r o g r a m m i n g F i n a l ' ,   N ' 5 . 0 . 0 ' ) 
 
 G O 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ A n a s a y f a ]   O N   
 
 
 
 I N S E R T   [ d b o ] . [ A n a s a y f a ]   ( [ I d ] ,   [ T e x t H e a d e r ] ,   [ T e x t ] ,   [ I m a g e ] )   V A L U E S   ( 1 ,   N ' G i r i _' ,   N ' M e r h a b a ,   b e n   T o p k a p 1  � n i v e r s i t e s i   B i l g i s a y a r   P r o g r a m c 1l 11( u z a k t a n   � r e t i m )   � r e n c i s i   B a t u h a n   � e l e b i   a y n 1  z a m a n d a   y a z 1l 1m   u z m a n   y a r d 1m c 1s 1  o l a r a k   B a s b u g   G r o u p   _i r k e t i n d e   � a l 1_m a k t a y 1m .   B u   p r o j e m e   v e   d i e r   p r o j e l e r i m e   0l e t i _i m   b � l � m � n d e k i   G i t H u b   l i n k i m   � z e r i n d e n   u l a _a b i l i r s i n i z .   P r o j e m d e n   v e   a m a � l a r 1n d a n   b a h s e t m e m   g e r e k i r s e   b u   p r o j e   f i n a l   � d e v i   o l a r a k   y a p t 11m   b i r   . N E T   C o r e   u y g u l a m a s 1.   C o d e F i r s t   y a k l a _1m 1  i l e   p r o j e   � z e r i n d e n   b i r   d a t a   o l u _t u r d u m .   B u   d a t a y 1  M o d e l s   l e r   e   y a z d 1m   v e   c o n t r o l l e r   l a r   a r a c 1l 11  i l e   V i e w   l a r   a   t a _1d 1m .   B u   s a y e d e   s a y f a l a r   � z e r i n d e n   y a z 1l a r 1m 1  g � r s e l l e r i m i   l i n k l e r i   v e   v i d e o l a r 1  g � r e b i l i y o r ,   v e   g � r � _m e   i � i n   b i l g i l e r i m i z i   g i r e b i l i y o r u z .   P r o j e n i n   a m a c 1n a   g e l i r s e k   d e   t � m   b u   y a p t 11m   i _l e m l e r i   k o d l a r 1  i l e   b i r l i k t e   s u n a r a k   b i r   p o r t f o l y o   m u   o l u _t u r m a s 1' ,   N ' ~ / P h o t o s / A n a s a y f a . p n g ' ) 
 
 I N S E R T   [ d b o ] . [ A n a s a y f a ]   ( [ I d ] ,   [ T e x t H e a d e r ] ,   [ T e x t ] ,   [ I m a g e ] )   V A L U E S   ( 2 ,   N ' ' ,   N ' ' ,   N ' ~ / P h o t o s / A n a s a y f a 2 . p n g ' ) 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ A n a s a y f a ]   O F F 
 
 G O 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ G a l e r i m ]   O N   
 
 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 1 ,   N ' ~ / P h o t o s / 1 . p n g ' ,   N ' h t t p s : / / w w w . y o u t u b e . c o m / e m b e d / H N o k f p T E y U 4 ' ) 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 2 ,   N ' ~ / P h o t o s / 2 . p n g ' ,   N ' h t t p s : / / w w w . y o u t u b e . c o m / e m b e d / 4 I g C 2 Q 5 - y D E ' ) 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 3 ,   N ' ~ / P h o t o s / 3 . p n g ' ,   N U L L ) 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 4 ,   N ' ~ / P h o t o s / 4 . p n g ' ,   N U L L ) 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 5 ,   N ' ~ / P h o t o s / 5 . p n g ' ,   N U L L ) 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 6 ,   N ' ~ / P h o t o s / 6 . p n g ' ,   N U L L ) 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 7 ,   N ' ~ / P h o t o s / 7 . p n g ' ,   N U L L ) 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 8 ,   N ' ~ / P h o t o s / 8 . p n g ' ,   N U L L ) 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 9 ,   N ' ~ / P h o t o s / 9 . p n g ' ,   N U L L ) 
 
 I N S E R T   [ d b o ] . [ G a l e r i m ]   ( [ I d ] ,   [ P h o t o ] ,   [ V i d e o ] )   V A L U E S   ( 1 0 ,   N ' ~ / P h o t o s / 1 0 . p n g ' ,   N U L L ) 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ G a l e r i m ]   O F F 
 
 G O 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ H a k k i m d a ]   O N   
 
 
 
 I N S E R T   [ d b o ] . [ H a k k i m d a ]   ( [ I d ] ,   [ T e x t ] ,   [ L i n k s ] )   V A L U E S   ( 1 ,   N ' S e p   2 0 2 2   -   M a y   2 0 2 2   Y a z 1l 1m   U z m a n   Y r d . ,   B a _b u   G r o u p   ,   0s t a n b u l 
 
 
 
 B i l g i   i _l e m   d e p a r t m a n 1  d e s t e k   b � l � m � n d e   b a _l a d 1m   v e   2   a y   
 
 s o n u n d a   a r - g e   y e   d o r u   y � n e l e n d i r i l d i m . 
 
 d e s t e k   d e   j i r a   a r a y � z � n �   k u l l a n a r a k   g e l e n   d e s t e k   t a l e p l e r i n i   
 
 y � n e t m e k   k a r _1l a m a k   v e   r a p o r l a m a   i _l e m l e r i n i   y a p t 1m . 
 
 b u   s � r e � t e   e r p   d e   _i r k e t   o l a r a k   c a n i a s   e r p   p r o g r a m 1n 1  
 
 k u l l a n 1y o r d u k   b u   p r o g r a m d a   t r o i a   d i l i n i   k u l l a n a r a k   e k r a n   
 
 g e l i _t i r m e   i _l e r i n e   v e   d e s t e k   t a l e p l e r i n e     b a k t 1m . 
 
 E r p   i l e   b e r a b e r   s q l   b e c e r i l e r i m i d e   o l d u k � a   g e l i _t i r d i m   � � n k i   
 
 _i r k e t   b i g   d a t a   s 1n 1  B 2 B   v e   E R P   p r o g r a m 1n d a   e t k i l i   _e k i l d e   
 
 k u l l a n 1y o r d u .   b e n d e   b u   s e b e p l e   s q l   t a r a f 1n d a   o t o m a t i k   
 
 � a l 1_a n   j o b   l a r   r a p o r l a m a   v e   v e r i   i z l e m e d e   k u l l a n 1l a b i l m e s i   
 
 i � i n   s t o r e d   p r o c e d u r e   l e r   o l u _t u r a r a k   S Q L   s o r g u   d i l i   v e   d a t a b a s e   y � n e t i m i   k o n u s u n d a   o l d u k � a   y e t e n e k l i   o l d u u m u   
 
 i s p a t l a d 1m .   b i r a z   d a h a   w e b   i _l e r i n i   c #   v e   c + +   d i l l e r i n i   
 
 � r e n m e k   i s t e d i i m   i � i n   f a r k l 1  i _l e r   a r a m a y a   b a _l a d 1m . ' ,   N U L L ) 
 
 I N S E R T   [ d b o ] . [ H a k k i m d a ]   ( [ I d ] ,   [ T e x t ] ,   [ L i n k s ] )   V A L U E S   ( 2 ,   N U L L ,   N ' h t t p s : / / w w w . y o u t u b e . c o m / e m b e d / P Y C o R n J k n _ c ' ) 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ H a k k i m d a ]   O F F 
 
 G O 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ P r o j e l e r i m ]   O N   
 
 
 
 I N S E R T   [ d b o ] . [ P r o j e l e r i m ]   ( [ I d ] ,   [ P r o j e c t N a m e ] ,   [ P r o j e c t D e s c r i p t i o n ] ,   [ P r o j e c t Y e a r ] )   V A L U E S   ( 1 ,   N ' D a t a   C o n n e c t i o n   a n d   L o g i n   P a g e ' ,   N ' L o g i n   P a g e   W i t h   A S P . N E T ' ,   N ' 2 0 2 2 ' ) 
 
 I N S E R T   [ d b o ] . [ P r o j e l e r i m ]   ( [ I d ] ,   [ P r o j e c t N a m e ] ,   [ P r o j e c t D e s c r i p t i o n ] ,   [ P r o j e c t Y e a r ] )   V A L U E S   ( 2 ,   N ' C a l c u l a t o r - W i n d o w s F o r m s ' ,   N ' M y   b e g i n n e r   c a l c u l a t o r .   1  m a k e   t h i s   w i t h   w i n d o w s   f o r m s ' ,   N ' 2 0 2 2 ' ) 
 
 I N S E R T   [ d b o ] . [ P r o j e l e r i m ]   ( [ I d ] ,   [ P r o j e c t N a m e ] ,   [ P r o j e c t D e s c r i p t i o n ] ,   [ P r o j e c t Y e a r ] )   V A L U E S   ( 3 ,   N ' W i n d o w s F o r m s P r o j e c t ' ,   N ' r a n d o m   n u m b e r s   a r e   g e n e r a t e d   o u t   o f   t h e m   a v e r a g e   i s   f o u n d ,   t h e   l a r g e s t   i s   f o u n d ,   h a l f   i s   f o u n d   a n d   t h e   p r i m e   o n e s   a r e   f o u n d ' ,   N ' 2 0 2 2 ' ) 
 
 I N S E R T   [ d b o ] . [ P r o j e l e r i m ]   ( [ I d ] ,   [ P r o j e c t N a m e ] ,   [ P r o j e c t D e s c r i p t i o n ] ,   [ P r o j e c t Y e a r ] )   V A L U E S   ( 4 ,   N ' P o r t f o l y o   u y g u l a m a s 1' ,   N ' A n a s a y f a ,   H a k k 1m d a ,   P r o j e l e r ,   G a l e r i   v e   i l e t i _i m   s a y f a l a r 1n d a n   o l u _a n   b i r   p r o j e ' ,   N ' 2 0 2 2 ' ) 
 
 I N S E R T   [ d b o ] . [ P r o j e l e r i m ]   ( [ I d ] ,   [ P r o j e c t N a m e ] ,   [ P r o j e c t D e s c r i p t i o n ] ,   [ P r o j e c t Y e a r ] )   V A L U E S   ( 5 ,   N ' B a s b u g   c r m ' ,   N ' c r m   k u r u l m a s 1  v e   e n t e g r a s y o n l a r 1' ,   N ' 2 0 2 2 ' ) 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ P r o j e l e r i m ]   O F F 
 
 G O 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ U l a s i m ]   O N   
 
 
 
 I N S E R T   [ d b o ] . [ U l a s i m ]   ( [ I d ] ,   [ N a m e ] ,   [ S u r n a m e ] ,   [ E M a i l ] ,   [ P h o n e N u m b e r ] ,   [ M e s s a g e ] )   V A L U E S   ( 4 ,   N ' B a t u h a n ' ,   N ' � e l e b i ' ,   N ' i l l i _ 1 @ o u t l o o k . c o m ' ,   N ' 0 5 3 0 5 6 2 3 2 3 4 ' ,   N ' T E S T 1 ' ) 
 
 I N S E R T   [ d b o ] . [ U l a s i m ]   ( [ I d ] ,   [ N a m e ] ,   [ S u r n a m e ] ,   [ E M a i l ] ,   [ P h o n e N u m b e r ] ,   [ M e s s a g e ] )   V A L U E S   ( 5 ,   N ' B a t u h a n ' ,   N ' � e l e b i ' ,   N ' b a t u h n @ o u t l o o k . c o m ' ,   N ' 0 5 3 0 5 6 2 3 2 3 4 ' ,   N ' T E S T 2   f a r k l 1  e   p o s t a ' ) 
 
 S E T   I D E N T I T Y _ I N S E R T   [ d b o ] . [ U l a s i m ]   O F F 
 
 G O 
 
 / * * * * * *   O b j e c t :     S t o r e d P r o c e d u r e   [ d b o ] . [ S p _ U l a s i m I n s e r t ]         S c r i p t   D a t e :   2 4 . 0 6 . 2 0 2 2   1 5 : 4 0 : 0 6   * * * * * * / 
 
 S E T   A N S I _ N U L L S   O N 
 
 G O 
 
 S E T   Q U O T E D _ I D E N T I F I E R   O N 
 
 G O 
 
 C R E A T E   p r o c e d u r e   [ d b o ] . [ S p _ U l a s i m I n s e r t ]     
 
 (     
 
       @ N a m e   n v a r c h a r ( 2 0 0 ) ,     
 
       @ S u r n a m e   n v a r c h a r ( 2 0 0 ) ,     
 
       @ E M a i l   n v a r c h a r ( 5 0 ) , 
 
       @ P h o n e N u m b e r   n v a r c h a r ( 2 0 ) , 
 
       @ M e s s a g e   n v a r c h a r ( 1 0 0 0 ) 
 
 )     
 
 A S 
 
 I F   N O T   E X I S T S ( S E L E C T   E M a i l   F R O M   U l a s i m   W H E R E   E M a i l   =   @ E M a i l ) 
 
 B E G I N   
 
 I N S E R T   I N T O   U l a s i m   ( N a m e ,   S u r n a m e ,   E M a i l ,   P h o n e N u m b e r ,   M e s s a g e )   V A L U E S ( @ N a m e , @ S u r n a m e , @ E M a i l , @ P h o n e N u m b e r , @ M e s s a g e )     
 
 E N D 
 
 G O 
 
 U S E   [ m a s t e r ] 
 
 G O 
 
 A L T E R   D A T A B A S E   [ D B F I N A L ]   S E T     R E A D _ W R I T E   
 
 G O 
 
 