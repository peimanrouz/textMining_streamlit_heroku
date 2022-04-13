import streamlit as st

from hazm import *
import re
import itertools
import operator


# st.code("This is st.code ... ")
# st.text("This is Text ... ")
# st.markdown("# This is Heading 1 in Markdown")
# st.title("This is a title")
# st.header("Header")
# st.subheader("SubHeader")
# st.latex(r'''
#             a+a^2+a^3+... = a^n 
#         ''')
# st.write("Can display many things")
# st.button("Click here")

Text = """آیا تا به حال به این موضوع اندیشیده‌اید که «موتورهای جستجوی» (Search Engines) نظیر «گوگل» (Google) و «بینگ» (Bing)، چگونه معانی و مفاهیم موجود در حجم عظیمی از اطلاعات سطح وب را درک می‌کنند و به راحتی قادر هستند اطلاعات مرتبط با پرس و جوی کاربران را بازیابی کنند؟ پاسخ به این سؤال، «متن کاوی» (Text Mining) است. متن کاوی، این توانایی را برای سیستم‌های کامپیوتری ایجاد می‌کند تا بتوانند اطلاعات معنادار را از «داده‌های متنی غیر ساخت‌یافته» (Unstructured Text Data) استخراج کنند.

در حال حاضر برآورد شده است که چیزی حدود 2٫۵ «کوینتیلیون» (Quintillion) بایت داده، روزانه در جهان تولید می‌‎شود (هر کوینتیلیون، برابر با 10 به توان 18 است). داده‌های متنی غیر ساخت‌یافته، بزرگترین منبع داده‌های تولید شده به وسیله انسان محسوب می‌شوند. حجم بسیار زیاد اطلاعات تولید شده، هم یک چالش و هم یک فرصت برای صاحبان مشاغل ایجاد می‌کند. این داده‌ها، از یک سو، به شرکت‌های تجاری این امکان را می‌دهند تا بتوانند بینش هوشمندانه و دانش مفیدی را در رابطه با دیدگاه مردم، نسبت به یک محصول یا سرویس خاص، کسب کنند. شرکت‌ها قادر خواهند بود از طریق اطلاعات به دست آمده از تحلیل ایمیل‌های مشتریان، نقدهای محصولات، مطالب شبکه‌های اجتماعی، بازخورد مشتریان و سایر موارد، ایده‌های جالبی در مورد بهبود محصولات و خدمات کنونی یا ارائه خدمات و محصولات جدید کسب کنند. از سوی دیگر، چالش بزرگ شرکت‌ها، چگونگی «پردازش» (Processing) این حجم از داده‌های غیر ساخت‌یافته است. اینجا است که اهمیت و نقش متن کاوی، در استراتژی بلند مدت شرکت‌ها مشخص می‌شود.

متن کاوی (Text Mining)

مقدمه‌ای بر متن کاوی
شاید مانند بسیاری از مفاهیم مرتبط با «پردازش زبان طبیعی» (Natural Language processing)، درک و فهم متن کاوی، ساز و کارها و مفاهیم آن کمی سخت به نظر بیاید. با این حال، در این متن سعی شده است با زبانی ساده، مقدمات متن‌کاوی، تکنیک‌ها و روش‌های مختلف آن و دلیل اهمیت متن کاوی شرح داده شود.

متن‌کاوی، که به آن «تحلیل متن» (Text Analysis) نیز گفته می‌شود، فرایند تبدیل داده‌های متنی غیر ساخت‌یافته به اطلاعات با معنا و عملی است. متن کاوی، از طریق شناسایی «موضوعات» (Topics)، «الگوها» (Patterns) و «کلمات کلیدی» (Keywords) مرتبط به کاربران اجازه‌ می‌دهد بدون نیاز به بررسی دستی حجم عظیمی از اطلاعات، دانش و اطلاعات مفیدی از داده‌های متنی غیر ساخت یافته به دست آورند.

به کمک متن‌کاوی، شرکت‌های تجاری قادر هستند تا مجموعه داده‌های بزرگ و پیچیده را به شکل ساده، سریع و بسیار مؤثری تجزیه و تحلیل کنند. همچنین، شرکت‌های بزرگ از این ابزار مفید بهره می‌برند تا حجم کارهای دستی و بعضا تکراری کارمندان و هدر رفت زمان با ارزش تیم‌های پشتیبانی و شاغل در شرکت را کاهش دهند.

متن کاوی (Text Mining)

برای واضح‌تر شدن موضوع، به این سناریو دقت کنید. فرض کنید شما یک شرکت نرم‌افزاری هستید که محصولات خود را به صورت سرویس‌های تحت وب ارائه می‌دهید. شما، به عنوان مدیر استراتژی شرکت قصد دارید تا بفهمید مشتریان از کدام یک از محصولات شما رضایت دارند، کدام محصول نیاز به بهبود دارد و چه ویژگی‌های جدیدی نیاز است به محصولات شرکت اضافه شود. در چنین حالتی، الگوریتم‌های متن کاوی می‌توانند موضوعات مهمی که در نظرات مشتریان نمایان می‌شوند را شناسایی و احساسات (منفی، مثبت و خنثی) آن‌ها در قبال یک محصول خاص را تجزیه و تحلیل کنند.

به عبارت دیگر، متن‌کاوی از طریق استخراج اطلاعات و دانش مفید از داده‌های سازمانی و غیرسازمانی مرتبط، منجر به ایجاد تصمیمات تجاری داده محور (Data-Driven Business Decisions) بهتر در شرکت‌ها می‌شوند. در این جا، شاید این سوال برای شما پیش بیاید که متن کاوی چگونه می‌تواند تمامی این موارد را محقق کند؟ پاسخ به این سوال در مفهوم «یادگیری ماشین» (Machine Learning) نهفته است.

یادگیری ماشین یکی از زیر شاخه‌های «هوش مصنوعی» (Artificial Intelligence) و هدف آن، تولید الگوریتم‌هایی است که کامپیوتر را قادر به یادگیری انجام وظایف، بر مبنای نمونه‌ها (داده‌ها) می‌کنند. مدل‌های یادگیری ماشین، پیش از آنکه مورد استفاده قرار بگیرند، باید توسط داده‌ها آموزش داده شوند. پس از آموزش، مدل‌های یادگیری ماشین قادر خواهند بود تا به طور خودکار و با درصد دقت مشخصی، در مورد داده‌های ورودی پیش‌بینی انجام دهند. وقتی که متن‌کاوی و یادگیری ماشین با هم ترکیب شوند، «تحلیل اتوماتیک متن» ممکن می‌شود.

متن کاوی (Text Mining)

اجازه دهید به مثال قبلی شرکت نرم‌افزاری تولید کننده محصولات تحت وب باز گردیم. فرض کنید که شما مایل هستید تا نظرات مشتریان را در موضوعات خاصی نظیر «طراحی واسط کاربری» (User Interface Design)، باگ‌ها، قیمت گذاری محصولات و پشتیبانی مشتریان دسته‌بندی کنید. اولین کاری که باید انجام دهید، آموزش یک «مدل دسته‌بند موضوع» (Topic Classifier Model) است. برای این کار، تعدادی نمونه آموزشی که منعکس کننده نظرات مشتریان است فراهم می‌شوند. سپس، این نمونه‌ها به عنوان ورودی به مدل آموزشی داده می‌شوند. پس از چند تکرار، مدل یاد خواهد گرفت که میان نظرات متعلق به دسته‌های مختلف تفاوت قائل شود. پس از پایان آموزش، مدل یادگیری دسته‌بندی موضوع قادر خواهد بود نظرات مشتریان به یکی از موضوعات مشخص شده تخصیص دهد.

باید توجه داشت که برای افزایش دقت مدل دسته‌بند موضوع، لازم است تا تعداد زیادی داده به عنوان داده آموزشی به سیستم داده شود. همچنین، داده‌های آموزشی حتما باید منعکس کننده دامنه مسأله‌ای باشند که مدل یادگیری برای حل آن ارائه شده است. پس از آشنایی با مفهوم متن کاوی، در مرحله بعد، تفاوت میان مفاهیم متن‌کاوی، «تحلیل کیفی متن» (Text Analysis) و «تحلیل کمی متن» (Text Analytics) مورد بررسی قرار می‌گیرد.

تفاوت میان مفاهیم متن کاوی، تحلیل کمی و کیفی متن
مفاهیم متن کاوی و تحلیل کیفی متن معمولا مترادف هستند. با این حال، مفهوم تحلیل کمی متن، تا حدودی متفاوت از دو مفهوم دیگر است. به اختصار، مدل‌های متن‌کاوی و مدل‌های تحلیل کمی متن سعی دارند مسأله‌ای یکسان (تحلیل خودکار داده‌های متنی خام) را به وسیله تکنیک‌های متفاوت حل کنند. تکنیک‌های متن کاوی، اطلاعات مرتبط درون یک متن را شناسایی می‌کنند و در نتیجه، نتایج کیفی تولید می‌کنند. در نقطه مقابل، هدف تکنیک‌های تحلیل کمی متن، یافتن الگوهای موجود در مجموعه‌های بزرگ داده است. در نتیجه، تکنیک‌های تحلیل کمی متن، معمولا نتایج کمی تولید می‌کنند. این تکنیک‌ها معمولا برای تولید داده‌نما، جدول و دیگر انواع گزارشات بصری مورد استفاده قرار می‌گیرند.

متن‌کاوی، مفاهیم آمار، زبان‌شناسی و یادگیری ماشین را ترکیب می‌کند تا مدل‌های هوشمندی برای یادگیری رفتار و مدل داده‌های آموزشی تولید کند. مدل هوشمند یادگیری ماشین به سیستم اجاز می‌دهد تا براساس داده‌های آموزشی، پیش‌بینی‌های جدیدی در مورد داده‌های ورودی جدید تولید کند (به عنوان نمونه، دسته‌بندی موضوعی داده‌های متنی غیر ساخت یافته جدید را پیش‌بینی کند). در نقطه مقابل، تحلیل کمی متن از نتایج حاصل از تحلیل‌های انجام شده توسط مدل‌های متن کاوی، برای تولید داده‌نما و انواع مختلفی از واسط‌های بصری داده استفاده می‌کند.

متن کاوی (Text Mining)

انتخاب مدل متن‌کاوی یا روش تحلیل کمی متن مناسب که بتواند نیازهای اطلاعاتی سازمان‌ها و یا شرکت‌های تجاری را محقق کند، بستگی زیادی به نوع اطلاعات در دسترس دارد. در غالب موارد، مدل‌های متن کاوی با روش‌های تحلیل کمی متن ترکیب و داده‌های حاوی محتوای متنی تحلیل می‌شوند. نتایج تحقیقات نشان داده است که چنین رویکردی، سبب تولید جواب‌های به مراتب بهتری نسبت به روش‌های دیگر تحلیل متن خواهد شد.

روش‌ها و تکنیک‌ها
تاکنون، روش‌ها و تکنیک‌های متفاوتی برای متن‌کاوی توسعه داده شده است. در این بخش سعی شده است تا تعریف مفید و مختصری از برخی روش‌های ساده و پیشرفته در حوزه متن کاوی ارائه شود.

روش‌های ساده متن کاوی
در ادامه، برخی از روش‌های ساده برای تحلیل داده‌های متنی آورده شده است.

روش‌های مبتنی بر تناوب کلمات (Word Frequency)
از روش‌های مبتنی بر تناوب کلمه برای شناسایی متناوب‌ترین لغات یا مفاهیم موجود در مجموعه‌ای از داده‌های متنی استفاده می‌شود. در کاربردهایی نظیر تحلیل نظرات مشتریان، گفتگوهای میان کاربران در شبکه‌های اجتماعی یا بازخورد مشتریان نسبت به یک محصول یا سرویس خاص، پیدا کردن کلماتی که پیش از همه در داده‌های متنی غیر ساخت یافته ظاهر شده‌اند، نقش مهمی در تولید اطلاعات با معنی و استخراج دانش از این داده‌ها خواهند داشت. به عنوان نمونه، در صورتی که لغاتی نظیر «گران» (Expensive)، «قیمت بیش از حد» (Overpriced) و «مبالغه در مورد امکانات» (Overrated)، به طور متناوب در نظرات مشتریان ظاهر شود، بهتر است که شرکت‌های تجاری ارائه دهنده این محصول یا خدمات قیمت‌ها (و یا بازار هدف این محصول یا سرویس) را کمی تغییر دهند.

روش‌های مبتنی بر باهم‌گذاری یا هم‌اتفاقی کلمات (Word Collocation)
اصطلاح باهم‌گذاری یا هم‌اتفاقی کلمات، به دنباله‌ای از کلمات یا مفاهیم اطلاق می‌شود که معمولا در یک داده متنی در کنار هم‌دیگر (همسایگی یکدیگر) ظاهر می‌شوند. شایع‌ترین نوع کلمات یا مفاهیم باهم‌گذاری (هم‌اتفاقی)، «دو کلمه‌ای‌ها» (Bigrams) و «سه کلمه‌ای‌ها» (Trigrams) هستند. دو کلمه‌ای‌ها، عباراتی دو کلمه‌ای هستند که معمولا در کنار یکدیگر اتفاق می‌افتند. به عنوان نمونه، در زبان انگلیسی عباراتی نظیر (Get Started)، (Save Time) و (Decision Making) نمونه‌ای از عبارات دو کلمه‌ای هستند. به طور مشابه، سه کلمه‌ای‌ها، عباراتی سه کلمه‌ای هستند که معمولا در بیشتر زمینه‌های موضوعی کنار یکدیگر اتفاق می‌افتند. به عنوان نمونه، در زبان انگلیسی عباراتی نظیر (Within Walking Distance) و (Keep In Touch) سه کلمه‌ای هستند.

شناسایی عبارات باهم‌گذاری یا هم‌اتفاق (و در نظر گرفتن آن‌ها به عنوان یک کلمه)، نقش مهمی در بهبود فرایند شناسایی واحدهای سازنده یک داده متنی غیر ساخت یافته خواهد داشت. چنین کاری، به مدل متن‌کاوی اجازه می‌دهد تا درک بهتری از ساختار معنایی موجود در داده‌های متنی پیدا کند و به تبع آن، نتایج دقیق‌تری از تحلیل‌های متن کاوی حاصل شود.

روش‌های مبتنی بر راهنمای لغات (Concordance)
اصطلاح راهنمای لغات، به لیستی از لغات یا مفاهیم موجود در یک سند به همراه مشخصه محل ظاهر شدن آن‌ها اطلاق می‌شود. از روش‌های مبتنی بر راهنمای لغات، برای بازشناسی یک «زمینه محتوایی‌» (Context) خاص استفاده می‌شود که یک کلمه یا مجموعه‌ای از کلمات در آن ظاهر شده‌اند. باید توجه داشت که ویژگی ذاتی زبان‌های انسانی، ابهام موجود در آن‌ها است. یکی از مشکلات موجود در پیاده‌سازی مدل‌های متن کاوی این است که یک کلمه می‌تواند در زمینه‌های محتوایی‌ متفاوتی استفاده شود. تحلیل‌های مبتنی بر راهنمای لغات از یک کلمه، به سیستم اجازه می‌دهد تا معنای دقیق یک کلمه در زمینه محتوایی که در آن ظاهر می‌شود را درک کند.

متن کاوی (Text Mining)

روش‌های پیشرفته متن کاوی
در ادامه، برخی از روش‌های پیشرفته تحلیل داده‌های متنی مورد بررسی قرار گرفته است.

دسته‌بندی متن (Text Classification)
دسته‌بندی متن، به فرایند برچسب‌گذاری یا اختصاص دادن یک (یا چند) دسته خاص به داده‌های متنی غیر ساخت یافته اطلاق می‌شود. دسته‌بندی متون، یکی از مؤلفه‌های اساسی در «پردازش زبان طبیعی» (Natural Language Processing) محسوب می‌شود و فرایند سازمان‌دهی و ساختاربندی داده‌های متنی پیچیده را آسان می‌کند. همچنین، فرایند دسته‌بندی متون نقش مهمی در شناسایی اطلاعات با معنا و استخراج دانش از داده‌های متنی دارد. یه کمک روش‌های دسته‌بندی متن، شرکت‌های تجاری و سازمان‌ها قادر خواهند بود انواع مختلفی از اطلاعات نظیر ایمیل‌ها و نظرات مشتریان را تحلیل کرده و از راه‌های سریع و مقرون به صرفه، اطلاعات و بینش مفیدی از داده‌های متنی به دست آورند.

متن کاوی (Text Mining)

در ادامه، مهم‌ترین کاربردهای دسته‌بندی متن نظیر «تحلیل موضوعی» (Topic Analysis)، «تحلیل احساسات» (Sentiment Analysis)، «تشخیص زبان» (Language Detection) و «تشخیص نیت یا هدف» (Intent Detection) مورد بررسی قرار می‌گیرند.

روش‌های تحلیل موضوعی متن: روش‌های تحلیل موضوعی متن به مدل متن‌کاوی کمک می‌کنند تا قالب محتوایی یا موضوع یک متن را درک کند. این دسته از روش‌ها، از جمله روش‌های اساسی برای سازمان‌دهی داده‌های متنی محسوب می‌شود. به عنوان نمونه، پیام درخواست پشتیبانی از سوی مشتریان ممکن است حاوی عبارتی نظیر «سفارش آنلاین من هنوز نرسیده است» (My Online Order Hasn’t Arrived) باشد. در چنین حالتی، پیام درخواست پشتیبانی مشتری می‌تواند در قالب محتوایی «مشکلات ارسال» (Shipping Issues) دسته‌بندی شود.
روش‌های تحلیل احساسات در متن: شامل روش‌های تحلیل احساسات نهفته در یک داده متنی است. فرض کنید که مدیر واحد پشتیبانی از مشتریان یک شرکت تجاری قصد دارد تا نظرات مرتبط با نرم‌افزار همراه شرکت را مورد بررسی قرار دهد. این شخص ممکن است دریابد که اغلب نظرات مشتریان در قالب موضوعی «واسط کاربری» (User Interface) یا «سهولت استفاده» (Ease of Use) دسته‌بندی شده‌اند. در چنین حالتی، مدیر واحد پشتیبانی، اطلاعات کافی را برای تصمیم‌گیری در مورد میزان رضایت مشتریان از محصول شرکت نخواهد داشت. تحلیل احساسات موجود در متن به مدل متن کاوی اجازه می‌دهد تا نظرات و احساسات نهفته در آن را درک و آن‌ها در قالب «مثبت» (Positive)، «منفی» (Negative) یا «خنثی» (Neutral) دسته‌بندی کند. تحلیل احساسات، کاربردهای مفیدی در سازمان‌ها و شرکت‌های تجاری دارد. به عنوان نمونه، در مورد پشتیبانی از مشتریان، یک شرکت تجاری از طریق تحلیل احساسات موجود در نظرات مشتریان، قادر خواهد بود مشتریان عصبانی را به سرعت شناسایی و به درخواست آن‌ها با اولویت بالاتری رسیدگی کند.
روش‌های تشخیص زبان متن: به مدل متن کاوی اجازه دسته‌بندی متن را بر اساس زبان می‌دهد. یکی از مهم‌ترین کاربردهای این دسته روش‌ها، هدایت اتوماتیک درخواست‌های پشتیبانی مشتریان در سراسر دنیا به نمایندگان شرکت در مناطق جغرافیایی مناسب است. به عنوان نمونه، درخواست کاربران ایرانی برای پشتیبانی، توسط کارمندان واحد پشتیبانی شرکت‌های تجاری در ایران پاسخ داده خواهد شد. خودکار کردن چنین فعالیتی بسیار ساده است و باعث بهره‌وری بهینه از زمان در شرکت‌های تجاری خواهد شد.
روش‌های تشخیص نیت یا هدف: از طریق روش‌های دسته‌بندی متن، نیت یا هدف نهفته در یک متن به طور خودکار شناسایی می‌شود. چنین قابلیتی در هنگام تحلیل گفتگوهای مشتریان بسیار سودمند خواهد بود. برای مثال، شرکت‌ها می‌توانند حجم عظیمی از پیام‌های دریافتی مشتریان را تحلیل کنند و از این طریق، افرادی که خواهان دریافت خدمات یا محصولات شرکت هستند را از کسانی که تمایل به لغو اشتراک خدمات یا محصولات خود دارند شناسایی کنند.
متن کاوی (Text Mining)

استخراج متن (Text Extraction)
استخراج متن یک تکنیک تحلیل کیفی متن است که ویژگی‌های خاصی نظیر «کلمات کلیدی» (Keywords)، «نام موجودیت‌های متنی» (Entity Names)، آدرس‌ها، ایمیل‌ها و سایر موارد را از داده‌های متنی استخراج می‌کند. این دسته از تکنیک‌ها، نقش مهمی در شناسایی اطلاعات کلیدی از داده‌های متنی غیر ساخت یافته دارند؛ اطلاعاتی که استخراج دستی آن‌ها از متن بسیار زمان‌گیر خواهد بود. در اغلب مواقع، ترکیب کردن روش‌های استخراج متن با روش‌های دسته‌بندی متن، برای تحلیل داده‌های متنی بسیار مفید است.

در ادامه، مهم‌ترین کاربردهای استخراج متن نظیر «استخراج کلمات کلیدی» (Keywords Extraction)، «بازشناسی موجودیت‌های نام‌گذاری شده» (Named Entity Recognition) و «استخراج ویژگی» (Feature Extraction) مورد بررسی قرار می‌گیرد.

روش‌های استخراج کلمات کلیدی: کلمات کلیدی، مرتبط‌ترین لغات موجود در یک داده متنی محسوب می‌شوند و می‌توانند برای خلاصه‌سازی محتویات آن‌ها مورد استفاده قرار بگیرند. استفاده از روش‌های استخراج کلمات کلیدی به مدل متن‌کاوی اجازه می‌دهند تا داده‌هایی که قرار است جستجو شوند را شاخص‌گذاری، محتویات متون را خلاصه‌سازی و متون را برچسب‌گذاری کند.
روش‌های بازشناسی موجودیت‌های نام‌گذاری شده: چنین روش‌هایی به مدل متن کاوی اجازه می‌دهند تا نام شرکت‌ها، سازمان‌ها و اشخاص را از یک داده متنی شناسایی و استخراج کنند.
روش‌های استخراج ویژگی: چنین روش‌هایی مدل متن‌کاوی را قادر می‌سازند تا ویژگی‌های خاص یک سرویس یا محصول را از میان مجموعه‌ای از داده‌های متنی شناسایی کنند. به عنوان نمونه، در صورتی که هدف، تحلیل مشخصات یک محصول باشد، از طریق این روش‌ها، ویژگی‌هایی نظیر رنگ، مدل و «نام تجاری» (Brand) قابل استخراج خواهد بود.
متن کاوی (Text Mining)

اهمیت مدل‌های متن کاوی
افراد و شرکت‌ها روزانه حجم عظیمی از داده‌ها را تولید می‌کنند. آمارها نشان می‌دهد که چیزی در حدود 80 درصد از داده‌های متنی غیر ساخت یافته‌اند؛ یعنی از طریق یک روش از پیش تعیین شده سازمان نیافته‌اند، قابل جستجو نیستند و مدیریت آن‌ها تقریبا غیر ممکن است. به عبارت دیگر، در قالب غیر ساخته یافته، این دسته داده‌ها حاوی اطلاعات مفید نیستند. سازمان‌دهی، طبقه‌بندی و استخراج اطلاعات مفید و بامعنا از داده‌های خام متنی، یکی از چالش برانگیزترین فعالیت‌ها در سازمان‌ها و شرکت‌های تجاری است.

در کاربردهای تجاری، داده‌های متنی غیر ساخت یافته می‌توانند شامل مواردی نظیر ایمیل‌ها، مطالب شبکه‌های اجتماعی، چت‌ها، درخواست‌های پشتیبانی از کاربران و نظرسنجی‌ها شوند. تحلیل و بررسی دستی این حجم از اطلاعات، قطعا به شکست منجر خواهد شد. چنین کاری نه تنها زمان‌بر و پر هزینه است، بلکه نادرست و غیر قابل مقیاس‌پذیر است. با این حال، مدل‌های متن کاوی روش‌های قابل اطمینان و مقرون به صرفه‌ای برای تحلیل دقیق، سریع و مقیاس‌پذیر داده‌های متنی هستند.

از جمله مهم‌ترین مزایای مدل‌های متن‌کاوی می‌توان به موارد زیر اشاره کرد:

«مقیاس‌پذیری» (Scalability): از طریق مدل‌های متن کاوی، سیستم قادر به تحلیل حجم عظیمی از داده‌ها، تنها در چند ثانیه خواهد بود. با خودکار کردن برخی از فرایندها در سازمان‌ها و شرکت‌های تجاری، از طریق به‌کارگیری مدل‌های متن‌کاوی، آن‌ها قادر خواهند بود وقت با ارزش خود را صرف دیگر کارها کنند و از این طریق، سازوکارهای تجاری سازنده‌ای را توسعه دهند.
«تحلیل بلادرنگ» (Real-Time Analysis): به کمک مدل‌های متن کاوی، شرکت‌ها قادر خواهند بود تا شرایط اضطراری نظیر تشخیص اوضاع بحرانی محتمل، کشف معایب طراحی محصول و یا نظرات منفی در مورد محصولات را به صورت آنی شناسایی و اولویت‌بندی کنند. چرا چنین ویژگی برای شرکت‌ها مهم است؟ چون امکان اتخاذ تصمیمات سریع (در هنگام مواجهه با بحران) را برای شرکت‌ها به ارمغان می‌آورد.
«معیار ثابت قدمی» (Consistent Criteria) در انجام کارها: مردم وقتی که با کارهای تکراری سر و کار دارند، احتمال اشتباه کردن آن‌ها افزایش می‌یابد. به عنوان نمونه، برچسب گذاری داده‌های متنی را در نظر بگیرید. برای اکثر گروه‌های انسانی شاغل در شرکت‌های تجاری و سازمان‌ها، طبقه‌بندی‌ دستی درخواست‌های پشتیبانی مشتریان، کاری طاقت‌فرسا و زمان‌بر است و در اکثر موارد، منجر به تولید خطا و تناقضات در سیستم خواهد شد. خودکار کردن چنین فعالیت‌هایی نه تنها باعث جلوگیری از هدر رفتن زمان می‌شود، بلکه نتایج بهتر و دقیق‌تری تولید می‌کند و سبب می‌شود که معیارهای یکنواختی در پاسخگویی به درخواست مشتریان اعمال شوند.
جمع‌بندی
درصد زیادی از داده‌های تولید شده در جهان، داده‌های متنی غیر ساخت یافته هستند. از سوی دیگر، داده‌های متنی بزرگترین منبع داده‌های انسانی تولید شده در سطح جهان محسوب می‌شوند. این حجم عظیم از اطلاعات خام و دست نخورده، مخزن بزرگی از دانش در دامنه‌های کاربردی مختلف به شمار می‌آیند. روش‌های متن کاوی به سیستم‌های هوشمند اجازه می‌دهند تا اطلاعات بامعنی و کلیدی را از «داده‌های متنی غیر ساخت‌یافته» استخراج کرده و فرایندهای استخراج دانش و سازمان‌دهی اطلاعات را خودکار کنند. در صورتی که بتوان اطلاعات مفید و کلیدی از این داده‌ها را استخراج و برای پیاده‌سازی سیستم‌های هوشمند اطلاعاتی استفاده کرد، شرکت‌های تجاری و سازمان‌ها بزرگترین ذی‌نفعان این فرایند خواهند بود."""
# Text


st.header("متن کامل")

st.write(Text)


Stopword = ['همچنان', 'مدت', 'چیز', 'سایر', 'جا', 'طی', 'کل', 'کنونی', 'بیرون','های', 'مثلا', 'کامل','ها', 'کاملا','گیرد','شود','است', 'آنکه', 
            'موارد', 'واقعی', 'امور', 'اکنون', 'بطور', 'بخشی', 'تحت', 'چگونه', 'عدم', 'نوعی', 'حاضر', 'وضع', 'مقابل', 'کنار', 'خویش', 'نگاه', 'درون',
            'زمانی', 'بنابراین', 'تو', 'خیلی', 'بزرگ', 'خودش', 'جز', 'اینجا', 'مختلف', 'توسط', 'نوع', 'همچنین', 'آنجا', 'قبل', 'جناح', 'اینها', 'طور', 'شاید',
            'ایشان', 'جهت', 'طریق', 'مانند', 'پیدا', 'ممکن', 'کسانی', 'جای', 'کسی', 'غیر', 'بی', 'قابل', 'درباره', 'جدید', 'وقتی', 'اخیر', 'چرا', 'بیش',
            'روی', 'طرف', 'جریان', 'زیر', 'آنچه', 'البته', 'فقط', 'چیزی', 'چون', 'برابر', 'هنوز', 'بخش', 'زمینه', 'بین', 'بدون', 'استفاد', 'همان', 'نشان',
            'بسیاری', 'بعد', 'عمل', 'روز', 'اعلام', 'چند', 'آنان', 'بلکه', 'امروز', 'تمام', 'بیشتر', 'آیا', 'برخی', 'علیه', 'دیگری', 'ویژه', 'گذشته', 'انجام',
            'حتی', 'داده', 'راه', 'سوی', 'ولی', 'زمان', 'حال', 'تنها', 'بسیار', 'یعنی', 'عنوان', 'همین', 'هبچ', 'پیش', 'وی', 'یکی', 'اینکه', 'وجود'
            , 'شما', 'پس', 'چنین', 'میان', 'مورد', 'چه', 'اگر', 'همه', 'نه', 'دیگر', 'آنها', 'باید', 'هر', 'او', 'ما', 'من', 'تا', 'نیز', 'اما', 
            'یک', 'خود', 'بر', 'یا', 'هم','ای', 'را','دارد', 'این',"می", 'با','دارد','،',',','.', 'آن', 'برای'
            ,'»','«','(',')','؟','?','شده_است','شده','داشت','مکن','آورد','آیند','کرد','آورده_شده_است','دهد','آورند','دهند', 'و', 'در', 'به', 'که', 'از',
            'اندیشیده_اید','کند','هستند','بتواند','برآورد','\u200eشود','شود','\u200e','شوند','خواهند_بود','آمده','یافته_است','ماند','بیاید',
            'رفت','کنید','هستید','دارید','دهید','دارند','بفهمید','داده_شوند','خواهد_گرفت','خواهد_بود','داده_است',
            'خواهد_شد','داده_شده_است','خواهند_داشت','خواهد_داشت','نرسیده_است','نرسیده_است','درخواست','نخواهد_داشت','داده_خواهد_شد','نیستند','نیافته_اند','بگیرید','رفتن','نیستند']
Stopword = set(Stopword)     # حذف استاپ وورد های تکراری
# Stopword

# st.sidebar.header("انتخاب تعداد جمله ی خلاصه از متن")

st.sidebar.header("استاپ وورد ها")

st.sidebar.dataframe(Stopword)


normalizer = Normalizer()
TextNor = normalizer.normalize(Text)
TextNor = TextNor.replace("\u200c", " ") 
# TextNor

TextIter = ''.join(ch for ch, _ in itertools.groupby(TextNor))
# TextIter

wordList = word_tokenize(TextIter)
# wordList


wordcount = {}
for i in wordList:
    if i not in Stopword:
        if i in wordcount.keys():
            wordcount[i] += 1
        else:
            wordcount[i] = 1


wordcount_sorted = sorted(wordcount.items(), key=operator.itemgetter(1), reverse=True)
# wordcount_sorted


Text_Tok_sentence = sent_tokenize(Text)
# Text_Tok_sentence


sentence_dict = {}
for i in Text_Tok_sentence:
    k = 0
    for j in wordcount.keys():
        if j in i:
            k += wordcount[j]
            sentence_dict[i] = k



sentence_dict = sorted(sentence_dict.items(), key=operator.itemgetter(1), reverse=True)


st.subheader("تعداد جمله ها برای خلاصه سازی متن را تعیین کنید")
sl = st.slider("Slide", min_value=2, max_value=20)
# st.write(sl)


abstractiveTexts = []
m = 0
for i in sentence_dict:
    m += 1
    abstractiveTexts.append(i[0])
    if m == sl:
        break



st.title(f"خلاصه متن در {sl} جمله")
st.write(abstractiveTexts)



paragraph = ""
c = 0
for i in sentence_dict:
    c += 1
    paragraph += i[0]
    paragraph += "   "
    if c == sl:
        break



st.title("خلاصه متن در یک پاراگراف")
st.write(paragraph)

#============================================


st.title("متن خود را برای خلاصه کردن وارد کنید ")


# your_text = st.text_input("Enter Your Text For Summarization : ")
your_text = st.text_area("Enter Your Text For Summarization : ")
# your_text = st.file_uploader("Upload Your Text File For Summarization : ")


st.header("متن کامل شما")

st.write(your_text)


normalizer = Normalizer()
your_textNor = normalizer.normalize(your_text)
your_textNor = your_textNor.replace("\u200c", " ") 


your_textNorIter = ''.join(ch for ch, _ in itertools.groupby(your_textNor))

yourWordList = word_tokenize(your_textNorIter)


yourWordcount = {}
for i in yourWordList:
    if i not in Stopword:
        if i in yourWordcount.keys():
            yourWordcount[i] += 1
        else:
            yourWordcount[i] = 1


yourWordcount_sorted = sorted(yourWordcount.items(), key=operator.itemgetter(1), reverse=True)


yourtext_Tok_sentence = sent_tokenize(your_text)



yourSentence_dict = {}
for i in yourtext_Tok_sentence:
    k = 0
    for j in yourWordcount.keys():
        if j in i:
            k += yourWordcount[j]
            yourSentence_dict[i] = k



yourSentence_dict_sorted = sorted(yourSentence_dict.items(), key=operator.itemgetter(1), reverse=True)


st.subheader("تعداد جمله ها برای خلاصه سازی متن را تعیین کنید")
sl2 = st.slider("Slide2", min_value=2, max_value=20)


yourAbstractiveTexts = []
m = 0
for i in yourSentence_dict_sorted:
    m += 1
    yourAbstractiveTexts.append(i[0])
    if m == sl2:
        break




# st.write("کمی درنگ بفرمایید")
# import time
# mybar = st.progress(0)

# for percent_complete in range(100):
#     time.sleep(0.02)
#     mybar.progress(percent_complete + 1)

# st.spinner()


# st.balloons()


st.title(f"خلاصه متن در {sl2} جمله")
st.write(yourAbstractiveTexts)



yourparagraph = ""
c = 0
for i in yourSentence_dict_sorted:
    c += 1
    yourparagraph += i[0]
    yourparagraph += "   "
    if c == sl2:
        break



st.title("خلاصه متن در یک پاراگراف")
st.write(yourparagraph)


#peimanRouznamehchi