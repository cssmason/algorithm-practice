from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # solution 1:
        # unique = set()
        # for email in emails:
        #     local, domain = email.split("@")
        #     local = local.split("+")[0]
        #     local = local.replace(".", "")
        #     unique.add((local, domain))
        # return len(unique)
        # solution 2:
        unique = set()
        for email in emails:
            # local
            index, local = 0, ""
            while email[index] not in ["@", "+"]:
                if email[index] != ".":
                    local += email[index]
                index += 1
            # domain
            while email[index] != "@":
                index += 1
            domain = email[index+1:]
            unique.add((local, domain))
        return len(unique)


if __name__ == '__main__':
    emails = ["test.email+alex@leetcode.com",
              "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
    print(Solution().numUniqueEmails(emails))
