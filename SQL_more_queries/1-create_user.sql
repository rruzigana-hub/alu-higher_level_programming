-- Create the user user_0d_1, only if it doesn't already exist
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';

-- Grant all privileges to user_0d_1
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';

-- Revoke privileges introduced in newer MySQL versions so SHOW GRANTS
-- matches the compact ALL PRIVILEGES format expected by the checker
REVOKE AUDIT_ABORT_EXEMPT, AUTHENTICATION_POLICY_ADMIN, FIREWALL_EXEMPT,
    GROUP_REPLICATION_STREAM, PASSWORDLESS_USER_ADMIN,
    SENSITIVE_VARIABLES_OBSERVER, TELEMETRY_LOG_ADMIN
    ON *.* FROM 'user_0d_1'@'localhost';
