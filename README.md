# SeeTree

ראשית, עבדתי על התרגיל כחמש שעות.
היה מעניין מאוד.

לצערי, יש לי איזה באג שטרם מצאתי ואני לא מצליח להחזיר את הפוליגון ו.או התמונות.
השתמשתי בספריית shapely
האובייקטים של הנקודה והפוליגון נראים כמו שאמורים ובנוסף אני מצליח למצוא נקודה שרירותית שהוצאתי מה viewer data של הVS בתוך פוליגון ספציפי אך משום מה שאני עובר על הדאטה שלנו זה לא מוצא.
גם אם אני קובע פוליגון אקראי גדול הוא מוצא את הנקודות בתוכו.

לכן, התעכבתי על על העניין המרכזי שעוד לא נפתר.
בנוסף, על לסדר את המבנה של הקוד. פונקציה של המודול של הפוליגון שמששתמש בפונקציה של המודול של תמונה - לקח לי קצת זמן לסדר את זה.

לא הספקתי ליישם את הפונקצייה האחרונה של 'כל הפוליגונים'.
אני אנסה להמשיך לדבג את זה.

** עדכון
get_image עובד. עבד גם קודם.
ציירתי את הנקודות והפוליגון בmatplotlib עבור פוליגון ספציפי. ראיתי שאכן אין בו נקודות (וכנראה בכמה אקראיים אחרים שבדקתי). הצלבתי עם הVS ומתצאתי פוליגון שיש בו ואני מקבל מערך של הנקודות.
הייתי צריך לשרטט כמה גרפים כדי לוודא נקודות במהירות ובלי הרבה לוגיקת קוד בהתחלה.
