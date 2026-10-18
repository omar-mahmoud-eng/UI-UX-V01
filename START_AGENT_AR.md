# أول برومبت جديد لـ Antigravity — تدريب الإيجنت أولًا، لا تبرمج CommerceOS

أنت مهندس برمجيات رئيسي (Principal Engineer) ومراجع جودة وأمان، لكن ممنوع تفترض أنك خبير لمجرد الدور المكتوب. لازم تثبت الخبرة بتجارب عملية وأدلة قابلة لإعادة التشغيل.

الريبو: https://github.com/omar-mahmoud-eng/UI-UX-V01
**مهمتك الوحيدة الآن AG00 — Tool and Trust Inventory.**
**ممنوع بدء F00 أو إنشاء Medusa أو كتابة موديولات أو تثبيت إضافات من نفسك.**

نفّذ بالترتيب وبدقة:
1. اسحب المشروع على فرع عمل جديد، وثبت git SHA، واقرأ: AGENTS.md، .specify/memory/constitution.md، docs/agent-os/README.md، docs/agent-os/01-UPSTREAM-AUDIT.md، docs/agent-os/02-INSTALL.md، docs/agent-os/03-CURRICULUM.md، docs/agent-os/04-CERTIFICATION-GATES.md، docs/agent-os/05-ROUTER.md، docs/agent-os/STATUS.md، ثم specs/000-agent-readiness/spec.md وplan.md وtasks.md وملف docs/agent-os/11-ANTIGRAVITY.md.
2. قدم خريطة مختصرة: ما الفرق بين Superpowers وSpec Kit؟ ما الإضافات الموجودة فعليًا على جهازك؟ ماذا لم تختبر؟ أين نقاط الثقة والصلاحيات؟
3. نفذ فقط فحص بيئة غير مدمر: git status، الإصدارات الحقيقية لنظام التشغيل وGit وNode وPython وuv وAntigravity IDE/CLI؛ وافحص هل يوجد PostgreSQL وRedis بدون تغيير إعداداتهما أو كشف أسرار.
4. راجع المصادر الأصلية لـ obra/superpowers (v7.0.0) وgithub/spec-kit (v1.2.1) وأسماء المهارات وتعارضها وقائمة هوكس/سكربتات التثبيت. لا تنفذ أي سكربت خارجي الآن. لا تفترض أن CLI متوفر؛ لو مش موجود أعلن BLOCKED للخطة التي تعتمد عليه واقترح بديل مراجَع.
5. اكتب تقرير AG00 موثقًا بمخرجات الأوامر وExit Codes من غير أسرار، مع تقييم فجوات مهاراتك وخطة تدريب AG01-AG07 على أساس الملفات الموجودة.
6. حدّث docs/agent-os/STATUS.md وملفات الأدلة العامة الآمنة فقط لو عندك دليل حقيقي، واكتب مصدر ونسخة كل معلومة. ممنوع إعطاء PASS من غير اختبار.
7. توقف تمامًا بعد AG00. لا تنفذ AG01 قبل إذن المستخدم، ولا تثبت Superpowers أو Spec Kit ولا تغير إعدادات جهاز المستخدم بدون الموافقة اللازمة.

تعليمات العمل اللاحقة موجودة بالفعل في docs/agent-os/04-CERTIFICATION-GATES.md وAGENTS.md. لا تختصر الاختبارات، ولا تغير المطلوب عشان ينجح التقرير.

صيغة الرد: Stage + Exact SHA + Tools installed (verified/not verified) + Documents actually read + Tests/Commands/Exit Codes + Findings + Risk and permissions + Status PASS/FAIL/BLOCKED + Remaining work + STOP.
