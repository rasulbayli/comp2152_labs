# ============================================================
#  WEEK 11 LAB — Q3: VULNERABILITY REPORT CLASS
#  COMP2152 — Rasul Dadashbayli
# ============================================================


class Finding:
    def __init__(self, severity, host, description):
        self.severity    = severity
        self.host        = host
        self.description = description

    def __str__(self):
        return f"[{self.severity}] {self.host} — {self.description}"


class Report:
    def __init__(self, team_name):
        self.team_name = team_name
        self.findings  = []

    def add_finding(self, finding):
        self.findings.append(finding)

    def get_by_severity(self, severity):
        return [f for f in self.findings if f.severity == severity]

    def summary(self):
        print(f"  Team: {self.team_name}")
        print(f"  Total findings: {len(self.findings)}")
        print(f"  HIGH:   {len(self.get_by_severity('HIGH'))}")
        print(f"  MEDIUM: {len(self.get_by_severity('MEDIUM'))}")
        print(f"  LOW:    {len(self.get_by_severity('LOW'))}")
        print("  " + "-" * 40)
        for f in self.findings:
            print(f"  {f}")


# --- Main ---
if __name__ == "__main__":
    print("=" * 60)
    print("  Q3: VULNERABILITY REPORT")
    print("=" * 60)

    report = Report("CyberHunters")

    findings_data = [
        Finding("HIGH",   "ssh.0x10.cloud",  "Default credentials admin:admin"),
        Finding("LOW",    "blog.0x10.cloud", "No HTTPS (cleartext)"),
        Finding("HIGH",   "ftp.0x10.cloud",  "Anonymous FTP access"),
        Finding("MEDIUM", "api.0x10.cloud",  "Server version exposed in headers"),
        Finding("LOW",    "cdn.0x10.cloud",  "Missing security headers"),
    ]

    print("\n--- Adding Findings ---")
    for f in findings_data:
        report.add_finding(f)
        print(f"  Added: {f}")

    print("\n--- Full Report ---")
    report.summary()

    print("\n--- HIGH Severity Only ---")
    for f in report.get_by_severity("HIGH"):
        print(f"  {f}")

    print("\n" + "=" * 60)
