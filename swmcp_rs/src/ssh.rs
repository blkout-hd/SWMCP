//! SSH client implementation using thrussh.

use std::sync::Arc;
use tokio::sync::Mutex;

/// SSH connection state.
pub struct SshConnection {
    host: String,
    port: u16,
    // TODO: Add actual SSH session
}

impl SshConnection {
    /// Create new SSH connection.
    pub fn new(host: String, port: u16) -> Arc<Mutex<Self>> {
        Arc::new(Mutex::new(Self { host, port }))
    }
    
    /// Connect to remote host.
    pub async fn connect(&mut self) -> anyhow::Result<()> {
        // TODO: Implement SSH connection using thrussh
        anyhow::bail!("SSH connection not yet implemented")
    }
    
    /// Execute command on remote host.
    pub async fn execute(&self, _command: &str) -> anyhow::Result<String> {
        // TODO: Implement command execution
        anyhow::bail!("Command execution not yet implemented")
    }
}
