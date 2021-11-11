class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        active = set()
        
        for email in emails :
            local, domain = email.split("@")
            active.add(local.replace(".", "").split("+")[0] + "@" + domain)
        
        return len(active)
