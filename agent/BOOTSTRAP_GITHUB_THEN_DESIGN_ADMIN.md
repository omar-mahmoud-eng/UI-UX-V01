# BOOTSTRAP GITHUB + START ADMIN UI/UX — SINGLE HANDOFF

أنت Lead UX Architect وGitHub Repository Maintainer وGoogle Stitch Automation Agent.

**الهدف المرحلي الأول:** تأكد من وجود حزمة `UI-UX-V01` كاملة داخل مستودع GitHub المصرح لك بالوصول إليه **دون حذف تاريخه أو استبدال ملفاته**. ثم ابدأ تنفيذ 638 شاشة UI/UX لوحة إدارة واحدة تلو الأخرى داخل Stitch، مستخدمًا `agent/START_ADMIN_STITCH_GITHUB.md` كالتعليمات الكاملة.

## STEP A — تحقق من المصدر ولا تفترض الرفع

1. افتح GitHub المرتبط بحسابي، وابحث بالاسم الدقيق `UI-UX-V01`؛ تحقق من الـowner والفرع الافتراضي والصلاحيات. لا تخترع عنوانًا أو تدعي امتلاك صلاحية push.
2. إذا كان الـRepo موجودًا وفيه ملفات الخطة، استنسخه، افحص `git status`, `git log -5 --oneline`, `git branch -a`، وشغّل `python scripts/verify_pack.py`.
3. إذا كان الـRepo موجودًا لكنه لا يحتوي الحزمة كاملة، استخرج أرشيف الـZIP المرفق باسم `UI-UX-V01_GitHub_Ready_760_Screens.zip` إن كان متاحًا في المحادثة أو ملفات العمل. وإلا استخدم **حزمة المصدر الأصلية** الموثقة على Google Drive: https://drive.google.com/file/d/1-b5zkEaWhIsQi8CEhkmqoD_pg4u901EE/view?usp=drivesdk. لا تدع أنك قرأت المصدر إن لم تتمكن من تنزيله فعليًا.
4. ارفع الملفين الرئيسيين `01_STOREFRONT/` و`02_ADMIN_PANEL/` وكامل ملفات `agent/`, `tracking/`, `scripts/`, `README.md`, `AGENTS.md`, `manifest.json`, `.github/workflows/validate-pack.yml` **عند توفر حزمة Repo Ready**. لا تعتبر ZIP مضغوطًا داخل المستودع بديلًا عن الملفات المفكوكة ما لم تقرر ذلك صراحةً.
5. لا تحذف أو تستبدل محتويات سابقة دون مراجعة الفرق. إن كان الريبو مشغولًا، استخدم branch مستقلًا وPull Request بدل force-push.
6. أجرِ فحص الأعداد: **638 admin + 122 storefront + 25 module**؛ تحقق من نجاح السكربت، ثم ادفع التغييرات بإذن المستخدم/صلاحياته المعتمدة واكتب **Commit SHA** الحقيقي ورابط repo والفرع. إن فشلت المصادقة، صرّح أن الرفع لم يحدث ولا تختلق SHA.

## STEP B — ابدأ تصميم لوحة الإدارة

اقرأ `agent/START_ADMIN_STITCH_GITHUB.md` **كاملًا** ثم نفّذ تفاصيله الإلزامية. اقرأ `DESIGN.md` والتعليمات العامة وكل وحدة معنية وكل ملف شاشة قبل إنشائها. لا تستبدل التصميم الفعلي بمخطط أو بكروت فارغة. استخدم Stitch SDK/MCP المتاح بالفعل، وليس اتصالًا مفترضًا.

ابدأ أولًا بتأسيس Admin Shell وفق الهوية، ثم أول شاشة من فهرس `02_ADMIN_PANEL/SCREENS_INDEX.md` بحسب `03_STITCH_BATCHES.md`، وسجّل معرف Stitch ورابط التصميم ونتيجة QA في `tracking/admin_execution_ledger.json`. تابع الشاشة التالية دون تكرار أو تجاوز ضمن جلسة العمل. عند نهاية حدود الأدوات/الجلسة، احفظ سجلًا قابلًا للاستكمال، ولا تدعِ عملًا في الخلفية.

**تعريف الإنجاز:** GitHub upload verified by commit+readback; ثم Stitch screens verified 1-by-1. المخرجات المصدرية ليست هي الشاشات المصممة.
