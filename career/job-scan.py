# Weekly job scan: pulls LIVE motion/design-engineer roles straight from company ATS boards
# (Greenhouse, Ashby, Lever). Run: python3 career/job-scan.py   Add company slugs to SLUGS as you find them.
import json, re, urllib.request, concurrent.futures as cf
SLUGS = """figma anthropic openai notion linear vercel stripe airbnb discord dropbox duolingo robinhood coinbase mercury ramp brex plaid rippling gusto asana airtable canva webflow framer lottiefiles rive intercom gong calendly datadog twilio reddit pinterest lyft instacart doordash spotify squarespace grammarly perplexity perplexityai runwayml runway elevenlabs deepgram anysphere cursor replit retool supabase clickup miro loom zapier attentive klaviyo braze sevenrooms cribl fireworksai cohere scaleai huggingface synthesia descript pitch raycast arc thebrowsercompany headspace calm peloton strava whoop oura ouraring nike newrelic puppet jamasoftware vacasa airship urbanairship cloudflare github gitlab hashicorp netlify sentry posthog mixpanel amplitude segment contentful sanity storyblok hightouch census dbtlabs databricks confluent mongodb elastic samsara motive servicetitan toast square block cashapp chime sofi wealthfront betterment affirm marqeta circle fireblocks chainalysis alchemy ledger phantom opensea uniswap uniswaplabs dapper dapperlabs flow eventbrite hubspot zendesk freshworks monday wrike smartsheet lucid lucidsoftware loom typeform jotform docusign dropboxsign pandadoc ironclad vanta drata secureframe wiz snyk 1password bitwarden okta auth0 tailscale fly render railway neon planetscale prisma clerk resend liveblocks tldraw excalidraw spline pitchcom gamma tome beautifulai jasper copyai writer glean harvey hebbia sierra decagon character characterai pika lumalabs ideogram midjourney suno udio heygen captions opusclip veed kapwing riverside frameio wistia vimeo mux livekit daily agora hume humeai vapi bland retellai assemblyai speechmatics superhuman shortwave reflect mem craft coda hex observable deepnote modal togetherai together groq cerebras sambanova anyscale baseten replicate octoai weightsandbiases wandb labelbox snorkel cresta gongio outreach salesloft apollo clay common room commonroom attio folk hightouch mutiny userpilot appcues pendo fullstory hotjar heap loom tellius""".split()
KW = re.compile(r"motion|animat|\brive\b|creative technolog|interactive design|design engineer|ux engineer", re.I)
def get(url):
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"}), timeout=15) as r:
            return json.load(r)
    except Exception: return None
def scan(slug):
    out=[]
    d=get(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs")
    if d and d.get("jobs"):
        for j in d["jobs"]:
            if KW.search(j["title"]): out.append(("gh",slug,j["title"],j.get("location",{}).get("name"),j.get("updated_at","")[:10],j.get("absolute_url")))
    d=get(f"https://api.ashbyhq.com/posting-api/job-board/{slug}?includeCompensation=true")
    if d and d.get("jobs"):
        for j in d["jobs"]:
            if KW.search(j["title"]): out.append(("ashby",slug,j["title"],f'{j.get("location")} remote={j.get("isRemote")}',j.get("publishedAt","")[:10],j.get("jobUrl"),(j.get("compensation") or {}).get("compensationTierSummary")))
    d=get(f"https://api.lever.co/v0/postings/{slug}?mode=json")
    if isinstance(d,list):
        for j in d:
            if KW.search(j.get("text","")):
                sr=j.get("salaryRange") or {}
                out.append(("lever",slug,j["text"],f'{j.get("categories",{}).get("location")} {j.get("workplaceType")}',"",j.get("hostedUrl"),f'{sr.get("min")}-{sr.get("max")} {sr.get("interval")}' if sr else None))
    return out
res=[]
with cf.ThreadPoolExecutor(32) as ex:
    for r in ex.map(scan, sorted(set(SLUGS))): res+=r
for r in res: print(" | ".join(str(x) for x in r))
print("TOTAL", len(res))
